#!/usr/bin/env python3
import json
import csv
import urllib.request
from pathlib import Path

URLS_FILE = 'recombinant-published-schema-urls.txt'
DICTS_DIR = 'dictionaries'
SCHEMA_DIR = Path('schema/tables')
EXAMPLES_DIR = Path('schema/examples')
BAD_EXAMPLES_DIR = Path('schema/bad_examples')
INQUIRY_FILE = Path('inquiry.yaml')
DATAPACKAGE_FILE = Path('datapackage.json')

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


def generate_example(schema, dataset_type, resource_name, lang, record):
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    path = EXAMPLES_DIR / f"{dataset_type}-{resource_name}_{lang}.csv"
    fields = [f['name'] for f in schema['fields']]
    row = {}
    for name in fields:
        value = record.get(name, '')
        if isinstance(value, list):
            value = ','.join(str(v) for v in value)
        row[name] = value
    with path.open('w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerow(row)
    return path


def generate_bad_example(schema, dataset_type, resource_name, lang, record):
    BAD_EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    path = BAD_EXAMPLES_DIR / f"{dataset_type}-{resource_name}_{lang}.csv"
    fields = [f['name'] for f in schema['fields']]
    bad_row = {}
    for name in fields:
        value = record.get(name, '')
        if isinstance(value, list):
            value = ','.join(str(v) for v in value)
        bad_row[name] = value
    if fields:
        bad_row[fields[0]] = 'INVALID'
    with path.open('w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerow(bad_row)
    return path


def generate_schemas(data, source, tasks):
    dataset_type = data.get('dataset_type', Path(source).stem)
    for res in data.get('resources', []):
        resource_name = res.get('resource_name') or ''
        example_record = res.get('example_record', {})
        en_fields, fr_fields = split_fields(res.get('fields', []))
        for lang, fields in [('en', en_fields), ('fr', fr_fields)]:
            schema = {
                'fields': [field_to_schema(f, lang) for f in fields],
                'missingValues': [''],
                'primaryKey': res.get('primary_key', [])
            }
            schema_path = write_schema(schema, dataset_type, resource_name, lang)
            example_path = generate_example(
                schema,
                dataset_type,
                resource_name,
                lang,
                example_record,
            )
            generate_bad_example(
                schema,
                dataset_type,
                resource_name,
                lang,
                example_record,
            )
            tasks.append({
                'path': str(example_path),
                'schema': str(schema_path)
            })
            print(f"Generated {schema_path}")


def write_inquiry(tasks):
    with INQUIRY_FILE.open('w', encoding='utf-8') as fh:
        fh.write('tasks:\n')
        for t in tasks:
            fh.write(f"  - path: {t['path']}\n")
            fh.write(f"    schema: {t['schema']}\n")

def write_datapackage(tasks):
    package = {'resources': []}
    for t in tasks:
        name = Path(t['path']).stem
        package['resources'].append({'name': name, 'path': t['path'], 'schema': t['schema']})
    with DATAPACKAGE_FILE.open('w', encoding='utf-8') as fh:
        json.dump(package, fh, indent=2)


def main():
    urls = [u.strip() for u in Path(URLS_FILE).read_text().splitlines() if u.strip()]
    generated = set()
    tasks = []
    for url in urls:
        local = fetch_url(url, Path(DICTS_DIR))
        generated.add(local.name)
        data = load_dict(local)
        generate_schemas(data, local, tasks)

    for f in Path(DICTS_DIR).glob('*.json'):
        if f.name not in generated:
            f.unlink()
    write_inquiry(tasks)
    write_datapackage(tasks)

if __name__ == '__main__':
    main()
