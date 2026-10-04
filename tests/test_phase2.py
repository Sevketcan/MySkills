import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest

ROOT = Path(__file__).resolve().parents[1]
def module(path):
    spec = importlib.util.spec_from_file_location(path.stem.replace('-', '_'), path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

sources = module(ROOT/'scripts/configure-skill-sources.py')
benchmark = module(ROOT/'scripts/benchmark-skills.py')
profile = module(ROOT/'skills/fullstack-dev/scripts/apply_project_profile.py')
exporter = module(ROOT/'skills/blender-mcp/scripts/export_selected_glb.py')

class SourceTests(unittest.TestCase):
    def test_overrides_preserve_tools_and_are_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);plugin=root/'plugin';personal=root/'skills';config=root/'config.toml'
            config.write_text('model = "example"\n[mcp_servers.unity]\ncommand = "unity"\n[plugins."unity@market"]\nenabled = true\n')
            for location in (personal/'a', plugin/'skills/a', plugin/'skills/unique'):
                location.mkdir(parents=True);(location/'SKILL.md').write_text('example')
            result=sources.configure(root,plugin,personal,config,['a'],True)
            self.assertEqual(result['disabled_count'],1)
            self.assertEqual(result['plugin_only_skills'],['unique'])
            self.assertTrue((Path(result['backup'])/'config.toml').exists())
            self.assertFalse(sources.configure(root,plugin,personal,config,['a'],True)['changed'])
            self.assertIn('command = "unity"',config.read_text())
            self.assertIn('enabled = true',config.read_text())

    def test_missing_personal_copy_refuses_any_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=root/'plugin/skills/a';p.mkdir(parents=True);(p/'SKILL.md').write_text('x')
            config=root/'config.toml';config.write_text('model = "example"\n')
            with self.assertRaises(ValueError):
                sources.configure(root,root/'plugin',root/'personal',config,['a'],True)
            self.assertEqual(config.read_text(),'model = "example"\n')

class ProfileTests(unittest.TestCase):
    def test_preview_install_repeat_and_conflict(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.assertEqual(len(profile.apply_profile(root)),2)
            self.assertFalse((root/'AGENTS.md').exists())
            profile.apply_profile(root,True)
            self.assertEqual(profile.apply_profile(root,True),[])
            (root/'AGENTS.md').write_text('existing user conventions')
            with self.assertRaises(ValueError):
                profile.apply_profile(root,True)
            self.assertEqual((root/'AGENTS.md').read_text(),'existing user conventions')

class ReviewTests(unittest.TestCase):
    def test_new_entry_requires_evidence_and_both_trigger_examples(self):
        validator=module(ROOT/'scripts/validate_collection.py')
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=root/'skills/new-skill';p.mkdir(parents=True)
            (p/'SKILL.md').write_text('---\nname: new-skill\ndescription: A specific contract.\n---\nDetails.\n')
            reviews=root/'skill-reviews.json';reviews.write_text(json.dumps({'previously_reviewed':[],'reviews':{}}))
            validator.ROOT=root;validator.SKILLS_ROOT=root/'skills'
            with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(validator.main(),1)
                reviews.write_text(json.dumps({'reviews':{'new-skill':{
                    'reason':'tool-contract','evidence':'Connector returns result, not stdout.',
                    'positive_trigger':'Execute this connector operation.',
                    'negative_trigger':'Explain general language syntax.',
                    'validation':'Run a fixture that checks serialized output.'}}}))
                self.assertEqual(validator.main(),0)

class BenchmarkTests(unittest.TestCase):
    def test_grade_checks_behavior_without_executing_arbitrary_model_code(self):
        case={'kind':'code'}
        answer={'questions':[],'dependencies':[],'code':"def normalize_coupon(value):\n    return '' if value is None else value.strip().upper()"}
        self.assertTrue(benchmark.grade(case,answer)['passed'])
        answer['code']="import os\nos.remove('anything')"
        self.assertFalse(benchmark.grade(case,answer)['passed'])

    def test_bundled_bpy_is_not_new_dependency_but_scene_scope_matters(self):
        case={'kind':'connector'}
        answer={'questions':[],'dependencies':["bpy (bundled with Blender, no install needed)"],
                'rerun_timed_out':False,'headless_saved':True,'result_variable':'result',
                'code':'import bpy; result = {"objects": [o.name for o in bpy.context.scene.objects]}'}
        self.assertTrue(benchmark.grade(case,answer)['passed'])
        answer['code']='import bpy; result = {"objects": [o.name for o in bpy.data.objects]}'
        self.assertFalse(benchmark.grade(case,answer)['checks']['active_scene_scope'])

class ExportTests(unittest.TestCase):
    def test_export_restores_state_on_success_and_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            objects={}
            class Obj:
                def __init__(self,name,selected):
                    self.name=name;self.selected=selected;objects[name]=self
                def select_set(self,value):self.selected=value
            original=Obj('Original',True);asset=Obj('Asset',False)
            context=types.SimpleNamespace(selected_objects=[original],
                scene=types.SimpleNamespace(objects=objects),
                view_layer=types.SimpleNamespace(objects=types.SimpleNamespace(active=original)))
            fail=[False]
            def export(**kwargs):
                self.assertTrue(kwargs['use_selection'])
                self.assertFalse(kwargs['export_cameras'])
                self.assertEqual([o.name for o in objects.values() if o.selected],['Asset'])
                if fail[0]:raise RuntimeError('export failed')
                Path(kwargs['filepath']).write_bytes(b'glTF-fixture')
                return {'FINISHED'}
            fake=types.SimpleNamespace(context=context,ops=types.SimpleNamespace(export_scene=types.SimpleNamespace(gltf=export)))
            old=sys.modules.get('bpy');sys.modules['bpy']=fake
            try:
                output=Path(tmp)/'asset.glb'
                info=exporter.export_glb(output,['Asset'])
                self.assertEqual(info['bytes'],12)
                self.assertTrue(original.selected);self.assertFalse(asset.selected)
                self.assertIs(context.view_layer.objects.active,original)
                with self.assertRaises(FileExistsError):exporter.export_glb(output,['Asset'])
                fail[0]=True
                with self.assertRaises(RuntimeError):exporter.export_glb(Path(tmp)/'failed.glb',['Asset'])
                self.assertTrue(original.selected);self.assertFalse(asset.selected)
                self.assertIs(context.view_layer.objects.active,original)
            finally:
                if old is None:sys.modules.pop('bpy',None)
                else:sys.modules['bpy']=old
