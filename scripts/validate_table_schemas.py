#!/usr/bin/env python3
import json
import os
import subprocess
from pathlib import Path
import requests

BASE_REPO = os.environ.get('GITHUB_REPOSITORY', '')
SHA = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
BASE_URL = f"https://raw.githubusercontent.com/{BASE_REPO}/{SHA}/"

EXAMPLES_DIR = Path('schema/examples')
TABLES_DIR = Path('schema/tables')

failures = 0
for csv_file in EXAMPLES_DIR.glob('*.csv'):
    schema_file = TABLES_DIR / f"{csv_file.stem}.json"
    if not schema_file.exists():
        continue
    schema_url = BASE_URL + str(schema_file).replace(' ', '%20')
    data_url = BASE_URL + str(csv_file).replace(' ', '%20')
    api_url = f"https://api.validata.etalab.studio/validate?schema={schema_url}&url={data_url}"
    r = requests.get(api_url)
    if r.status_code != 200:
        print(f"Validation failed for {csv_file}: HTTP {r.status_code}")
        failures += 1
        continue
    resp = r.json()
    valid = resp.get('report', {}).get('valid')
    if not valid:
        print(f"Validation errors for {csv_file}:")
        print(json.dumps(resp.get('report', {}), indent=2))
        failures += 1
    else:
        print(f"Validated {csv_file} successfully")

if failures:
    raise SystemExit(f"{failures} schema validations failed")

