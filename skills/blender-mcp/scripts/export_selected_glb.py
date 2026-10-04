"""Export an explicitly selected asset set without saving or changing the source .blend."""
import json
from pathlib import Path

def export_glb(output, object_names=None, overwrite=False):
    import bpy
    target = Path(output).expanduser().resolve()
    if target.suffix.lower() != '.glb':
        raise ValueError('Output must have a .glb extension')
    if target.exists() and not overwrite:
        raise FileExistsError(f'Output already exists: {target}')
    previous = list(bpy.context.selected_objects)
    active = bpy.context.view_layer.objects.active
    if object_names is None:
        objects = previous
    else:
        objects = []
        for name in object_names:
            obj = bpy.context.scene.objects.get(name)
            if obj is None:
                raise ValueError(f'Object is not in the active scene: {name}')
            objects.append(obj)
    if not objects:
        raise ValueError('Select an asset or supply object_names')
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        for obj in previous:
            obj.select_set(False)
        for obj in objects:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = objects[0]
        outcome = bpy.ops.export_scene.gltf(filepath=str(target), export_format='GLB',
                                           use_selection=True, export_apply=True,
                                           export_cameras=False, export_lights=False,
                                           export_yup=True, check_existing=False)
        if 'FINISHED' not in outcome or not target.is_file():
            raise RuntimeError('Exporter did not produce the requested file')
        return {'path': str(target), 'objects': [obj.name for obj in objects],
                'bytes': target.stat().st_size}
    finally:
        for obj in objects:
            obj.select_set(False)
        for obj in previous:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = active

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--objects', nargs='+')
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:])
    summary = export_glb(args.output, args.objects, args.overwrite)
    print(json.dumps(summary))
