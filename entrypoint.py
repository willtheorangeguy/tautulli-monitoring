"""Load the existing API key from a mounted secret, then run upstream code."""
import os
import runpy
import sys
from pathlib import Path

os.environ['TAUTULLI_API_KEY'] = Path('/run/secrets/tautulli_api_key').read_text().strip()
if not os.environ['TAUTULLI_API_KEY']:
    raise RuntimeError('Tautulli API secret is empty')
sys.path.insert(0, '/app')
runpy.run_module('tautulli_exporter', run_name='__main__')
