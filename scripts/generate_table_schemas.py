#!/usr/bin/env python3
import json
import csv
import urllib.request
from pathlib import Path

URLS_FILE = 'recombinant-published-schema-urls.txt'
DICTS_DIR = 'dictionaries'
SCHEMA_DIR = Path('schema/tables')
EXAMPLES_DIR = Path('schema/examples')

TYPE_MAP = {
    'text': 'string',
    'int': 'integer',
    'money': 'number',
    'date': 'date',
    'year': 'year',
}


def fetch_url(url: str, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = Path(url.split('?')[0]).name
    if not name.endswith('.json'):
        name += '.json'
    dest = dest_dir / name
    with urllib.request.urlopen(url) as r:
        dest.write_bytes(r.read())
    return dest


def load_dict(path: Path):
    with path.open('r', encoding='utf-8') as fh:
        return json.load(fh)


def map_type(ds_type: str) -> str:
    return TYPE_MAP.get(ds_type, 'string')


def split_fields(fields):
    en_fields = []
    fr_fields = []
    for f in fields:
        fid = f.get('id', '')
        if fid.endswith('_en'):
            en_fields.append(f)
        elif fid.endswith('_fr'):
            fr_fields.append(f)
        else:
            en_fields.append(f)
            fr_fields.append(f)
    return en_fields, fr_fields


def field_to_schema(field, lang: str):
    name = field['id']
    label = field.get('label', {}).get(lang) or field.get('label', {}).get('en') or field.get('label', {}).get('fr') or name
    description = field.get('description', {}).get(lang, '')
    ds_type = field.get('datastore_type', '')
    schema = {
        'name': name,
        'title': label,
        'description': description,
        'type': map_type(ds_type)
    }
    constraints = {}
    obligation = field.get('obligation', {}).get(lang) or field.get('obligation', {}).get('en') or ''
    if obligation.lower().startswith('mandatory') or obligation.lower().startswith('obligatoire'):
        constraints['required'] = True
    choices = field.get('choices')
    if choices:
        constraints['enum'] = list(choices.keys())
    if constraints:
        schema['constraints'] = constraints
    return schema


def write_schema(schema, dataset_type, resource_name, lang):
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)
    path = SCHEMA_DIR / f"{dataset_type}-{resource_name}_{lang}.json"
    with path.open('w', encoding='utf-8') as fh:
        json.dump(schema, fh, ensure_ascii=False, indent=2)
    return path


def generate_example(schema, dataset_type, resource_name, lang):
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    path = EXAMPLES_DIR / f"{dataset_type}-{resource_name}_{lang}.csv"
    fields = [f['name'] for f in schema['fields']]
    rows = []
    for i in range(1, 6):
        row = {}
        for f in schema['fields']:
            ct = f.get('constraints', {})
            if 'enum' in ct:
                row[f['name']] = ct['enum'][0]
            else:
                t = f['type']
                if t in ('integer', 'year'):
                    row[f['name']] = str(2000 + i)
                elif t == 'number':
                    row[f['name']] = str(i * 10.5)
                elif t == 'date':
                    row[f['name']] = f'2025-01-0{i}'
                else:
                    row[f['name']] = f"{f['name']}_{i}"
        rows.append(row)
    with path.open('w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return path


def generate_schemas(data, source):
    dataset_type = data.get('dataset_type', Path(source).stem)
    for res in data.get('resources', []):
        resource_name = res.get('resource_name') or ''
        en_fields, fr_fields = split_fields(res.get('fields', []))
        for lang, fields in [('en', en_fields), ('fr', fr_fields)]:
            schema = {
                'fields': [field_to_schema(f, lang) for f in fields],
                'missingValues': ['']
            }
            schema_path = write_schema(schema, dataset_type, resource_name, lang)
            generate_example(schema, dataset_type, resource_name, lang)
            print(f"Generated {schema_path}")


def main():
    urls = [u.strip() for u in Path(URLS_FILE).read_text().splitlines() if u.strip()]
    generated = set()
    for url in urls:
        local = fetch_url(url, Path(DICTS_DIR))
        generated.add(local.name)
        data = load_dict(local)
        generate_schemas(data, local)

    for f in Path(DICTS_DIR).glob('*.json'):
        if f.name not in generated:
            f.unlink()

if __name__ == '__main__':
    main()
