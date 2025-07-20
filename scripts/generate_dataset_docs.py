#!/usr/bin/env python3
import json
import os
import urllib.request
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class ChoiceSet:
    def __init__(self, name):
        self.name = name
        self.values = []
        self.cardinality = 0

    def add(self, code, en, fr):
        self.values.append({'code': code, 'label_en': en, 'label_fr': fr})
        self.cardinality += 1

URLS_FILE = 'recombinant-published-schema-urls.txt'
DICTS_DIR = 'dictionaries'
DOCS_DIR = 'docs/reference'
TEMPLATE = 'scripts/template.md.j2'


def git_commit():
    try:
        import subprocess
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
    except Exception:
        return 'UNKNOWN'


def fetch_url(url, dest_dir):
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = Path(url.split('?')[0]).name
    if not name.endswith('.json'):
        name += '.json'
    dest = dest_dir / name
    with urllib.request.urlopen(url) as r:
        dest.write_bytes(r.read())
    return dest


def load_dict(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_dataset(data, source, env):
    tmpl = env.get_template(Path(TEMPLATE).name)
    context = {
        'dataset_type': data.get('dataset_type', ''),
        'title': data.get('title', {}),
        'notes': data.get('notes', {}),
        'resources': [],
        'generation': {
            'timestamp_iso': datetime.utcnow().isoformat(timespec='seconds'),
            'source_display': source,
            'commit': git_commit(),
            'tool_version': 'simple-1'
        },
        'all_choice_sets': [],
        'validation': {'passed': True, 'warnings': []},
    }
    for r in data.get('resources', []):
        res = {
            'title': r.get('title', {}),
            'anchor': r.get('resource_name', ''),
            'fields': []
        }
        for f in r.get('fields', []):
            field = {
                'id': f.get('id'),
                'label': f.get('label', {}),
                'description': f.get('description', {}),
                'datastore_type': f.get('datastore_type', ''),
                'required': f.get('obligation', {}).get('en', '').lower() == 'mandatory',
                'max_chars': f.get('max_length'),
                'validation': f.get('validation'),
                'choice_set': None
            }
            choices = f.get('choices')
            if choices:
                cs = ChoiceSet(f['id'])
                for code, val in choices.items():
                    if isinstance(val, dict):
                        cs.add(code, val.get('en', ''), val.get('fr', ''))
                    else:
                        cs.add(code, str(val), str(val))
                field['choice_set'] = cs
            res['fields'].append(field)
        context['resources'].append(res)
    return tmpl.render(**context)


def main():
    env = Environment(loader=FileSystemLoader('scripts'))
    urls = [u.strip() for u in Path(URLS_FILE).read_text().splitlines() if u.strip()]
    DOCS_PATH = Path(DOCS_DIR)
    DOCS_PATH.mkdir(parents=True, exist_ok=True)
    generated_docs = set()
    generated_dicts = set()
    for url in urls:
        local_path = fetch_url(url, Path(DICTS_DIR))
        generated_dicts.add(local_path.name)
        data = load_dict(local_path)
        md = render_dataset(data, str(local_path), env)
        dataset_type = data.get('dataset_type', Path(local_path).stem)
        out_file = DOCS_PATH / f"{dataset_type}.md"
        out_file.write_text(md, encoding='utf-8')
        generated_docs.add(out_file.name)

    # remove docs no longer referenced
    for f in DOCS_PATH.glob('*.md'):
        if f.name not in generated_docs:
            f.unlink()

    # remove dictionaries no longer referenced
    dicts_path = Path(DICTS_DIR)
    for f in dicts_path.glob('*.json'):
        if f.name not in generated_dicts:
            f.unlink()


if __name__ == '__main__':
    main()
