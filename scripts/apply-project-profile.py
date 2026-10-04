#!/usr/bin/env python3
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[1] / 'skills/fullstack-dev/scripts/apply_project_profile.py'), run_name='__main__')
