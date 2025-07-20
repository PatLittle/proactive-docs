#!/usr/bin/env python3
import json, os, sys, re, hashlib, datetime, subprocess, csv
from pathlib import Path
import click
from jsonschema import Draft7Validator
from jinja2 import Environment, FileSystemLoader
from urllib.parse import urlparse

TOOL_VERSION = "0.2.0"

class ChoiceSet:
    def __init__(self, name, origin, field_ids):
        self.name = name
        self.origin = origin  # 'inline' or filename/url
        self.field_ids = set(field_ids)
        self.values = []  # dicts: code,label_en,label_fr, minister_history
        self.has_minister_history = False
    @property
    def cardinality(self):
        return len(self.values)
    @property
    def fields(self):
        return sorted(self.field_ids)
    def add_value(self, v):
        if v.get('minister_history'): self.has_minister_history = True
        self.values.append(v)

def load_json(source: str):
    if re.match(r'^https?://', source):
        import urllib.request
        with urllib.request.urlopen(source) as r:
            return json.load(r), source
    p = Path(source)
    with p.open('r', encoding='utf-8') as f:
        return json.load(f), str(p)

def load_text(source: str):
    if re.match(r'^https?://', source):
        import urllib.request
        with urllib.request.urlopen(source) as r:
            return r.read().decode('utf-8')
    return Path(source).read_text(encoding='utf-8')

def load_schema(schema_path: str):
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def git_commit():
    try:
        return subprocess.check_output(['git','rev-parse','--short','HEAD']).decode().strip()
    except Exception:
        return "UNKNOWN"

def normalize_text_obj(val):
    if isinstance(val, dict):
        en = val.get('en') or val.get('EN') or ""
        fr = val.get('fr') or val.get('FR') or en
    else:
        en = str(val)
        fr = str(val)
    return {'en': en, 'fr': fr}

def parse_choice_file(path_or_url):
    text = load_text(path_or_url)
    # Try JSON
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            rows = []
            for code, val in obj.items():
                if isinstance(val, dict):
                    rows.append({'code': code, 'label_en': val.get('en') or '', 'label_fr': val.get('fr') or val.get('en') or ''})
                else:
                    rows.append({'code': code, 'label_en': str(val), 'label_fr': str(val)})
            return rows
        elif isinstance(obj, list):
            rows = []
            for item in obj:
                if isinstance(item, dict):
                    code = item.get('code') or item.get('id')
                    en = item.get('en') or item.get('label_en') or item.get('label') or ''
                    fr = item.get('fr') or item.get('label_fr') or en
                    if code:
                        rows.append({'code': code, 'label_en': en, 'label_fr': fr})
            return rows
    except json.JSONDecodeError:
        pass
    # Fallback CSV
    rows = []
    reader = csv.reader(text.splitlines())
    headers = None
    for r in reader:
        if not r: continue
        if headers is None and any(h.lower() in ('code','en','fr','label') for h in r):
            headers = [h.lower() for h in r]
            continue
        if headers:
            row = dict(zip(headers, r))
            code = row.get('code') or row.get('id')
            en = row.get('en') or row.get('label') or ''
            fr = row.get('fr') or en
        else:
            code = r[0]
            en = r[1] if len(r) > 1 else ''
            fr = r[2] if len(r) > 2 else en
        rows.append({'code': code, 'label_en': en, 'label_fr': fr})
    return rows

def extract_fields(resource, dataset_type, choice_sets):
    out = []
    for f in resource.get('fields', []):
        id_ = f.get('id') or f.get('datastore_id')
        label = normalize_text_obj(f.get('label', id_))
        desc = normalize_text_obj(f.get('description', ""))
        validation = normalize_text_obj(f.get('validation', ""))
        obligation = normalize_text_obj(f.get('obligation', ""))
        required = (obligation.get('en','').lower().startswith('mandat') or f.get('excel_required') is True)
        datastore_type = f.get('datastore_type', '')
        max_chars = f.get('max_chars')
        choice_set = None
        if f.get('choices') or f.get('choices_file'):
            if f.get('choices_file'):
                from urllib.parse import urlparse
                stem = Path(urlparse(f['choices_file']).path).stem
                cs_name = f"{stem}"
                if cs_name not in choice_sets:
                    choice_sets[cs_name] = ChoiceSet(cs_name, f['choices_file'], [id_])
                    rows = parse_choice_file(f['choices_file'])
                    for row in rows:
                        choice_sets[cs_name].add_value({
                            'code': row['code'],
                            'label_en': row['label_en'],
                            'label_fr': row['label_fr'],
                            'minister_history': None,
                            'minister_history_count': 0
                        })
                else:
                    choice_sets[cs_name].field_ids.add(id_)
                choice_set = choice_sets[cs_name]
            elif f.get('choices'):
                cs_name = f"{dataset_type}__{id_}"
                if cs_name not in choice_sets:
                    choice_sets[cs_name] = ChoiceSet(cs_name, 'inline', [id_])
                    for code, val in f['choices'].items():
                        if isinstance(val, dict):
                            label_en = val.get('en') or val.get('label_en') or val.get('label') or ''
                            label_fr = val.get('fr') or val.get('label_fr') or label_en
                            history = val.get('ministers') or val.get('minister_history')
                            mh_list = []
                            if isinstance(history, list):
                                for h in history:
                                    if isinstance(h, dict):
                                        mh_list.append({
                                            'en': h.get('en') or h.get('label_en') or h.get('name_en') or '',
                                            'fr': h.get('fr') or h.get('label_fr') or h.get('name_fr') or (h.get('en') or ''),
                                            'start': h.get('start') or h.get('start_date'),
                                            'end': h.get('end') or h.get('end_date')
                                        })
                            choice_sets[cs_name].add_value({
                                'code': code,
                                'label_en': label_en,
                                'label_fr': label_fr,
                                'minister_history': mh_list if mh_list else None,
                                'minister_history_count': len(mh_list) if mh_list else 0
                            })
                        else:
                            s = str(val)
                            choice_sets[cs_name].add_value({
                                'code': code,
                                'label_en': s,
                                'label_fr': s,
                                'minister_history': None,
                                'minister_history_count': 0
                            })
                else:
                    choice_sets[cs_name].field_ids.add(id_)
                choice_set = choice_sets[cs_name]
        out.append({
            'id': id_, 'label': label, 'description': desc, 'validation': validation if (validation['en'] or validation['fr']) else None,
            'required': required, 'datastore_type': datastore_type, 'max_chars': max_chars, 'choice_set': choice_set
        })
    return out

def write_choice_docs(choice_sets, out_root):
    choices_dir = Path(out_root) / 'choices'
    choices_dir.mkdir(parents=True, exist_ok=True)
    index_rows = []
    for cs in sorted(choice_sets.values(), key=lambda c: c.name.lower()):
        filename = f"{cs.name}.md"
        cs.output_filename = filename
        path = choices_dir / filename
        with path.open('w', encoding='utf-8') as f:
            f.write(f"# Choice Set: {cs.name}\n\n")
            f.write(f"**Origin:** {cs.origin}\n\n")
            f.write(f"**Fields Using This Set:** {', '.join(cs.fields)}\n\n")
            f.write(f"**Values (n={cs.cardinality}):**\n\n")
            if cs.has_minister_history:
                f.write("| Code | Label (EN) | Label (FR) | Minister History Count |\n")
                f.write("|------|------------|------------|-----------------------|\n")
            else:
                f.write("| Code | Label (EN) | Label (FR) |\n")
                f.write("|------|------------|------------|\n")
            for v in cs.values:
                if cs.has_minister_history:
                    f.write(f"| `{v['code']}` | {v['label_en']} | {v['label_fr']} | {v.get('minister_history_count',0)} |\n")
                else:
                    f.write(f"| `{v['code']}` | {v['label_en']} | {v['label_fr']} |\n")
            if cs.has_minister_history:
                f.write("\n## Minister History Details\n\n")
                for v in cs.values:
                    if v.get('minister_history'):
                        f.write(f"### Code `{v['code']}` – {v['label_en']} / {v['label_fr']}\n\n")
                        f.write("| Seq | Minister (EN) | Minister (FR) | Start | End |\n")
                        f.write("|-----|---------------|---------------|-------|-----|\n")
                        for idx, mh in enumerate(v['minister_history'], start=1):
                            f.write(f"| {idx} | {mh['en']} | {mh['fr']} | {mh['start'] or ''} | {mh['end'] or ''} |\n")
            f.write("\n*Auto-generated choice set document.*\n")
        index_rows.append(cs)
    with (choices_dir / 'index.md').open('w', encoding='utf-8') as idx:
        idx.write('# Choice Sets Index\n\n')
        idx.write('| Choice Set | Values | Fields | Standalone Doc | Has Minister History |\n')
        idx.write('|------------|--------|--------|----------------|----------------------|\n')
        for cs in index_rows:
            idx.write(f"| {cs.name} | {cs.cardinality} | {', '.join(cs.fields)} | {cs.output_filename} | {'Yes' if cs.has_minister_history else 'No'} |\n")

def generate_doc(src, data, validator, schema_obj, out_dir):
    dataset_type = data.get('dataset_type')
    filename = f"{dataset_type}.md" if dataset_type else f"dict_{hashlib.sha1(src.encode()).hexdigest()[:8]}.md"
    warnings = []
    passed = True
    if schema_obj:
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            passed = False
            for e in errors[:50]:
                warnings.append(f"Schema error at {'/'.join(map(str,e.path)) or '<root>'}: {e.message}")
    for r in data.get('resources', []):
        for f in r.get('fields', []):
            if f.get('choices') and f.get('choices_file'):
                warnings.append(f"Field {f.get('id') or f.get('datastore_id')} has both choices and choices_file.")
    choice_sets = {}
    resources = []
    for r in data.get('resources', []):
        r_title = normalize_text_obj(r.get('title', dataset_type))
        res_fields = extract_fields(r, dataset_type, choice_sets)
        anchor = re.sub(r'[^a-z0-9]+','-', r_title['en'].lower()).strip('-')
        resources.append({'title': r_title, 'fields': res_fields, 'anchor': anchor})
    write_choice_docs(choice_sets, out_dir)
    all_choice_sets_context = []
    for cs in sorted(choice_sets.values(), key=lambda c: c.name):
        all_choice_sets_context.append({
            'name': cs.name,
            'fields': cs.fields,
            'cardinality': cs.cardinality,
            'output_filename': f"choices/{cs.output_filename}",
        })
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)))
    tmpl = env.get_template('template.md.j2')
    context = {
        'dataset_type': dataset_type,
        'title': normalize_text_obj(data.get('title', dataset_type)),
        'notes': normalize_text_obj(data.get('notes', "")),
        'resources': resources,
        'all_choice_sets': all_choice_sets_context,
        'generation': {
            'timestamp_iso': datetime.datetime.utcnow().replace(microsecond=0).isoformat(),
            'source_display': src,
            'commit': git_commit(),
            'tool_version': TOOL_VERSION
        },
        'validation': {
            'passed': passed,
            'warnings': warnings
        }
    }
    md = tmpl.render(**context)
    out_path = Path(out_dir) / filename
    out_path.write_text(md, encoding='utf-8')
    return passed, warnings, len(choice_sets)

@click.command()
@click.option('--source', '-s', required=True, multiple=True, help='Path or URL to recombinant JSON (repeatable)')
@click.option('--schema', default='schema/recombinant-schema.json', help='Path to validation schema')
@click.option('--out-dir', default='docs/reference', show_default=True, help='Directory for generated markdown')
@click.option('--fail-on-error/--no-fail-on-error', default=True)
def main(source, schema, out_dir, fail_on_error):
    schema_obj = None
    validator = None
    if Path(schema).exists():
        schema_obj = load_schema(schema)
        validator = Draft7Validator(schema_obj)
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    failures = 0
    for src in source:
        data, src_display = load_json(src)
        passed, warnings, cs_count = generate_doc(src_display, data, validator, schema_obj, out_dir)
        click.echo(f"Wrote doc for {src_display} (validation: {'PASS' if passed else 'FAIL'}) with {cs_count} choice set(s)")
        if not passed:
            failures += 1
    if failures and fail_on_error:
        sys.exit(1)

if __name__ == '__main__':
    main()
