#!/usr/bin/env python3
"""Validate generated table schemas using the Validata API."""

import argparse
import json
import os
import subprocess
import time
from pathlib import Path

import requests


def main(tables_dir: str, examples_dir: str, delay: float, schema_file: str = None, data_file: str = None):
    """Validate CSV examples against their table schemas via Validata."""

    base_repo = os.environ.get('GITHUB_REPOSITORY', '')
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    base_url = f"https://raw.githubusercontent.com/{base_repo}/{sha}/"

    tables_path = Path(tables_dir)
    examples_path = Path(examples_dir)

    failures = 0
    pairs = []
    if schema_file and data_file:
        pairs.append((Path(data_file), Path(schema_file)))
    else:
        for csv_file in examples_path.glob('*.csv'):
            sfile = tables_path / f"{csv_file.stem}.json"
            if not sfile.exists():
                continue
            pairs.append((csv_file, sfile))

    for csv_file, schema_path in pairs:
        schema_url = base_url + str(schema_path).replace(' ', '%20')
        data_url = base_url + str(csv_file).replace(' ', '%20')
        api_url = (
            f"https://api.validata.etalab.studio/validate?schema={schema_url}&url={data_url}"
        )
        r = requests.get(api_url)
        if r.status_code != 200:
            print(f"Validation failed for {csv_file}: HTTP {r.status_code}")
            failures += 1
        else:
            resp = r.json()
            valid = resp.get('report', {}).get('valid')
            if not valid:
                print(f"Validation errors for {csv_file}:")
                print(json.dumps(resp.get('report', {}), indent=2))
                failures += 1
            else:
                print(f"Validated {csv_file} successfully")
        time.sleep(delay)

    if failures:
        raise SystemExit(f"{failures} schema validations failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate example data against table schemas")
    parser.add_argument(
        "--tables-dir",
        default="schema/tables",
        help="Directory containing generated table schemas",
    )
    parser.add_argument(
        "--examples-dir",
        default="schema/examples",
        help="Directory containing example CSV files",
    )
    parser.add_argument(
        "--schema-file",
        help="Schema file to validate against",
    )
    parser.add_argument(
        "--data-file",
        help="CSV file to validate",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=10.0,
        help="Seconds to wait between API calls",
    )
    args = parser.parse_args()
    main(args.tables_dir, args.examples_dir, args.delay, args.schema_file, args.data_file)

