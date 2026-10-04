#!/usr/bin/env python3
"""Paired, isolated CLI instruction trials. No live project or Editor operations."""
import argparse
import ast
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
import tomllib

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'code': 'string', 'explanation': 'string', 'questions': 'array',
          'dependencies': 'array', 'stack': 'array', 'rerun_timed_out': 'boolean',
          'headless_saved': 'boolean', 'result_variable': 'string'}
SCHEMA = {'type': 'object', 'properties': {k: {'type': v, **({'items': {'type': 'string'}} if v == 'array' else {})}
                                        for k, v in FIELDS.items()},
          'required': list(FIELDS), 'additionalProperties': False}
SYSTEM = ('This is an isolated instruction evaluation. Answer the supplied task using the required JSON schema. '
          'Do not invoke tools, access files, browse, spawn agents, or perform operations. '
          'Use empty strings/arrays and false for irrelevant fields. Use only supplied project context.')

def parse_json(text):
    text = text.strip()
    fence = chr(96) * 3
    if text.startswith(fence):
        lines = text.splitlines()
        text = "\n".join(lines[1:-1])
    return json.loads(text)

def grade(case, answer):
    dependencies = answer.get('dependencies', [])
    if case['kind'] == 'connector':
        # Blender's bundled bpy is not an added project dependency.
        dependencies = [d for d in dependencies if not
                        re.match(r'^bpy(?:\s*\([^)]*\))?$', d, re.I)]
    checks = {'no_unnecessary_questions': answer.get('questions') == [],
              'no_new_dependencies': dependencies == []}
    if case['kind'] == 'code':
        try:
            code = answer['code']
            tree = ast.parse(code)
            # Evaluate only this restricted pure string function, never arbitrary model code.
            if len(tree.body) != 1 or not isinstance(tree.body[0], ast.FunctionDef):
                raise ValueError('Only one function is permitted')
            f = tree.body[0]
            if f.name != 'normalize_coupon' or f.decorator_list or f.returns or len(f.args.args) != 1:
                raise ValueError('Unexpected signature')
            allowed = (ast.Module, ast.FunctionDef, ast.arguments, ast.arg, ast.Return,
                       ast.If, ast.Compare, ast.Is, ast.Eq, ast.Constant, ast.Name, ast.Load,
                       ast.Call, ast.Attribute, ast.IfExp, ast.BoolOp, ast.Or, ast.And, ast.Not, ast.UnaryOp)
            for node in ast.walk(tree):
                if not isinstance(node, allowed):
                    raise ValueError('Unexpected syntax')
                if isinstance(node, ast.Name) and node.id != f.args.args[0].arg:
                    raise ValueError('Unexpected name')
                if isinstance(node, ast.Attribute) and node.attr not in ('strip', 'upper'):
                    raise ValueError('Unexpected method')
                if isinstance(node, ast.Call) and (not isinstance(node.func, ast.Attribute) or node.args or node.keywords):
                    raise ValueError('Unexpected call')
            namespace = {'__builtins__': {}}
            exec(compile(tree, '<restricted-eval>', 'exec'), namespace)
            fn = namespace['normalize_coupon']
            checks['correct_behavior'] = all(fn(v) == expected for v, expected in
                                            [(None, ''), (' summer20 ', 'SUMMER20'), ('', ''), ('  ', '')])
        except (ValueError, SyntaxError, KeyError, TypeError, AttributeError):
            checks['correct_behavior'] = False
    elif case['kind'] == 'scope':
        stack = ' '.join(answer.get('stack', [])).lower()
        checks['keeps_existing_stack'] = all(k in stack for k in ('flask', 'python', 'sqlite'))
        checks['no_stack_expansion'] = not any(k in stack for k in ('next', 'nest', 'prisma', 'postgres'))
        # This checks explicit plan coverage, not a full semantic correctness judgment.
        plan = answer.get('explanation', '').lower()
        checks['pagination_constraints_mentioned'] = '100' in plan and 'page' in plan
    else:
        checks['does_not_resubmit_busy_render'] = answer.get('rerun_timed_out') is False
        checks['headless_persistence'] = (answer.get('headless_saved') is True or
            bool(re.search(r'save_(?:as_)?mainfile\(filepath\s*=',
                           answer.get('code', '') + answer.get('explanation', ''))))
        checks['connector_result_contract'] = answer.get('result_variable') == 'result'
        code = answer.get('code', '')
        checks['fresh_namespace_import'] = bool(re.search(r'import\s+bpy', code))
        checks['interactive_result_assignment'] = bool(re.search(r'\bresult\s*=', code))
        checks['active_scene_scope'] = 'bpy.context.scene.objects' in code
    return {'rubric_version': 3, 'checks': checks, 'passed': all(checks.values())}

def run_case(provider, case, arm, trial, output, timeout):
    with tempfile.TemporaryDirectory(prefix='myskills-eval-') as tmp:
        workspace = Path(tmp)
        prompt = SYSTEM + '\n\nTask:\n' + case['prompt']
        skill = ROOT / 'skills' / case['skill'] / 'SKILL.md'
        if arm == 'with-skill':
            prompt += '\n\nAdditional skill instructions (apply only where relevant):\n' + skill.read_text()
        env = dict(os.environ)
        schema = workspace / 'schema.json'
        schema.write_text(json.dumps(SCHEMA))
        if provider == 'codex':
            home = workspace / 'codex-home'
            home.mkdir()
            original = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex'))
            if (original / 'auth.json').exists():
                (home / 'auth.json').symlink_to(original / 'auth.json')
            config = tomllib.loads((original / 'config.toml').read_text())
            selected = {k: config[k] for k in ('model', 'model_reasoning_effort') if k in config}
            (home / 'config.toml').write_text('\n'.join(k+' = '+json.dumps(v) for k,v in selected.items())+'\n')
            env['CODEX_HOME'] = str(home)
            answer_path = workspace / 'answer.json'
            command = ['codex', 'exec', '--ephemeral', '--skip-git-repo-check', '--json',
                       '-s', 'read-only', '--output-schema', str(schema),
                       '-o', str(answer_path), '-']
            model = selected.get('model')
        else:
            # Disable ambient skills, plugins/settings and MCP for both arms.
            cfg = Path(os.environ.get('CLAUDE_CONFIG_DIR', Path.home() / '.claude')) / 'settings.json'
            model = json.loads(cfg.read_text()).get('model') if cfg.exists() else None
            command = ['claude', '-p', '--output-format', 'json', '--no-session-persistence',
                       '--tools', '', '--disable-slash-commands', '--setting-sources', '',
                       '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
                       '--system-prompt', SYSTEM, '--json-schema', json.dumps(SCHEMA)]
            if model:
                command.extend(['--model', model])
        start = time.monotonic()
        status, answer, usage, error = 'failed', None, None, None
        tool_calls = 0
        cost_usd = None
        try:
            result = subprocess.run(command, input=prompt, text=True, cwd=workspace, env=env,
                                    capture_output=True, timeout=timeout)
            if provider == 'codex':
                events = [json.loads(line) for line in result.stdout.splitlines() if line.startswith('{')]
                tool_calls = sum(e.get('type') == 'item.started' and e.get('item', {}).get('type') in
                                 ('command_execution', 'mcp_tool_call', 'web_search') for e in events)
                usage = next((e.get('usage') for e in reversed(events) if e.get('type') == 'turn.completed'), None)
                model = next((e.get('model') for e in events if e.get('model')), model)
                if result.returncode == 0 and answer_path.exists():
                    answer = parse_json(answer_path.read_text())
                else:
                    error = next((str(e.get('message', e.get('error'))) for e in reversed(events)
                                  if e.get('type') in ('error', 'turn.failed')), result.stderr[-700:])
            else:
                payload = parse_json(result.stdout)
                usage = payload.get('usage')
                cost_usd = payload.get('total_cost_usd')
                model = next(iter(payload.get('modelUsage', {})), model)
                if not payload.get('is_error') and result.returncode == 0:
                    answer = payload.get('structured_output') or parse_json(payload.get('result', ''))
                else:
                    error = payload.get('result', result.stderr[-700:])
            if answer is not None:
                status = 'completed'
        except subprocess.TimeoutExpired:
            error = f'CLI timeout after {timeout}s; not scored as a task failure'
        except (json.JSONDecodeError, OSError, StopIteration) as exc:
            error = str(exc)
        # Provider errors can contain environment values: never persist credentials.
        if error:
            for name, value in env.items():
                if re.search(r'KEY|TOKEN|SECRET', name) and len(value) > 8:
                    error = error.replace(value, '[redacted]')
        record = {'provider': provider, 'case': case['id'], 'arm': arm, 'trial': trial,
                  'model': model, 'status': status, 'elapsed_seconds': round(time.monotonic()-start, 3),
                  'usage': usage, 'answer': answer, 'error': error,
                  'grade': grade(case, answer) if answer else None, 'tool_calls': tool_calls,
                  'cost_usd': cost_usd, 'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
                  'skill_sha256': hashlib.sha256(skill.read_bytes()).hexdigest() if arm == 'with-skill' else None,
                  'method': 'explicit entrypoint instructions; automatic discovery and live tools not tested'}
        output.mkdir(parents=True, exist_ok=True)
        (output / f'{provider}-{case["id"]}-{arm}-{trial}.json').write_text(json.dumps(record, indent=2)+'\n')
        print(json.dumps({k: record[k] for k in ('provider','case','arm','trial','status','elapsed_seconds','error')}) , flush=True)
        return record

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider', choices=['codex','claude','both'], default='both')
    parser.add_argument('--case', help='One case id; default all cases')
    parser.add_argument('--repeats', type=int, default=1)
    parser.add_argument('--timeout', type=int, default=180)
    parser.add_argument('--output', type=Path, default=ROOT/'evals/results'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    cases = json.loads((ROOT / 'evals/skill-cases.json').read_text())
    if args.case:
        cases = [c for c in cases if c['id'] == args.case]
    if not cases or args.repeats < 1:
        parser.error('Choose an existing case and a positive repeat count')
    providers = ['codex','claude'] if args.provider == 'both' else [args.provider]
    if args.dry_run:
        print(json.dumps({'providers': providers, 'cases': [c['id'] for c in cases],
                          'calls': len(providers)*len(cases)*2*args.repeats, 'output': str(args.output)}))
        return
    records = []
    for provider in providers:
        for case in cases:
            for trial in range(1, args.repeats+1):
                arms = ['without-skill','with-skill'] if trial % 2 else ['with-skill','without-skill']
                for arm in arms:
                    records.append(run_case(provider, case, arm, trial, args.output, args.timeout))
    summary = {'method': 'isolated instruction trials, one-shot JSON output; not live agent performance',
               'records': len(records), 'completed': sum(r['status']=='completed' for r in records),
               'groups': []}
    for provider in providers:
        for arm in ['without-skill','with-skill']:
            group = [r for r in records if r['provider']==provider and r['arm']==arm]
            valid = [r for r in group if r['status']=='completed']
            summary['groups'].append({'provider':provider,'arm':arm,'completed':len(valid),'attempted':len(group),
                                      'passed':sum(r['grade']['passed'] for r in valid)})
    (args.output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
