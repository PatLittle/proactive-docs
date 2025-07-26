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

# Collect CSV/schema pairs for frictionless inquiry
INQUIRY_TASKS = []

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
    """Return identical field lists for EN and FR schemas."""
    # Older versions generated language-specific schemas that only included
    # fields ending with the matching language suffix.  This resulted in the
    # EN and FR table schemas having different structures.  We now keep the
    # field structure identical for both languages and only localise the
    # labels and descriptions.
    return fields, fields


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


def write_examples(schema, dataset_type, resource_name, lang, example_record):
    """Write example and bad example CSV files for a resource."""

    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    BAD_EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)

    fields = [f["name"] for f in schema["fields"]]
    example_path = EXAMPLES_DIR / f"{dataset_type}-{resource_name}_{lang}.csv"
    bad_path = BAD_EXAMPLES_DIR / f"{dataset_type}-{resource_name}_{lang}.csv"

    # Normal example
    row = {}
    for name in fields:
        value = example_record.get(name, "")
        if isinstance(value, list):
            value = ",".join(str(v) for v in value)
        row[name] = value
    with example_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerow(row)

    # Bad example - change value of the first field
    bad_row = row.copy()
    first_field = schema["fields"][0]
    fname = first_field["name"]
    if "constraints" in first_field and "enum" in first_field["constraints"]:
        bad_row[fname] = "INVALID"
    elif first_field["type"] in ("integer", "year", "number"):
        bad_row[fname] = "notanumber"
    elif first_field["type"] == "date":
        bad_row[fname] = "not-a-date"
    else:
        bad_row[fname] = ""
    with bad_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerow(bad_row)

    INQUIRY_TASKS.append((str(example_path), str(SCHEMA_DIR / f"{dataset_type}-{resource_name}_{lang}.json")))

    return example_path, bad_path


def generate_schemas(data, source):
    dataset_type = data.get('dataset_type', Path(source).stem)
    for res in data.get('resources', []):
        resource_name = res.get('resource_name') or ''
        en_fields, fr_fields = split_fields(res.get('fields', []))
        example = res.get('example_record', {})
        primary_key = res.get('primary_key', [])
        for lang, fields in [('en', en_fields), ('fr', fr_fields)]:
            schema = {
                'fields': [field_to_schema(f, lang) for f in fields],
                'missingValues': ['']
            }
            if primary_key:
                schema['primaryKey'] = primary_key
            schema_path = write_schema(schema, dataset_type, resource_name, lang)
            write_examples(schema, dataset_type, resource_name, lang, example)
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

    if INQUIRY_TASKS:
        with Path('inquiry.yaml').open('w', encoding='utf-8') as fh:
            fh.write('tasks:\n')
            for csv_path, schema_path in INQUIRY_TASKS:
                fh.write(f'  - path: {csv_path}\n')
                fh.write(f'    schema: {schema_path}\n')

if __name__ == '__main__':
    main()

