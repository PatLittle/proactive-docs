#!/usr/bin/env python3
import json, os, sys, re, hashlib, datetime, subprocess, csv
from pathlib import Path
import click
from jsonschema import Draft7Validator
from jinja2 import Environment, FileSystemLoader
from urllib.parse import urlparse
from glob import glob

TOOL_VERSION = "0.4.0"

###############################################################################
# Models
###############################################################################

class ChoiceSet:
    """
    Represents either a global choice set (from choices_file) or an inline enum.
    Global sets: name = basename (stem) of file/URL (no dataset prefix).
    Inline sets: name = <dataset_type>__<field_id>.
    """
    def __init__(self, name, origin, is_global):
        self.name = name
        self.origin = origin          # 'inline' or original file/url
        self.is_global = is_global
        self.field_ids = set()
        self.values = []              # list of dicts: code, label_en, label_fr, minister_history, minister_history_count
        self.has_minister_history = False
        self.content_hash = None

    @property
    def cardinality(self):
        return len(self.values)

    def add_field(self, field_id):
        self.field_ids.add(field_id)

    def add_value(self, v):
        if v.get('minister_history'):
            self.has_minister_history = True
        self.values.append(v)

    def compute_hash(self):
        canon = json.dumps(
            sorted(
                [
                    {
                        "code": v["code"],
                        "label_en": v["label_en"],
                        "label_fr": v["label_fr"],
                        "minister_history": v.get("minister_history") or []
                    }
                    for v in self.values
                ],
                key=lambda x: x["code"]
            ),
            ensure_ascii=False,
            separators=(",", ":")
        )
        self.content_hash = hashlib.sha1(canon.encode("utf-8")).hexdigest()


###############################################################################
# Utility functions
###############################################################################

def git_commit():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
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

def load_json(source: str):
    p = Path(source)
    with p.open('r', encoding='utf-8') as f:
        return json.load(f), str(p)

def fetch_remote(url: str, dest_dir: Path) -> Path:
    import urllib.request
    dest_dir.mkdir(parents=True, exist_ok=True)
    parsed = urlparse(url)
    stem = Path(parsed.path).name or f"remote-{hashlib.sha1(url.encode()).hexdigest()[:8]}.json"
    if not stem.endswith(".json"):
        stem += ".json"
    local_path = dest_dir / stem
    with urllib.request.urlopen(url) as r:
        local_path.write_text(r.read().decode('utf-8'), encoding='utf-8')
    return local_path

def parse_choice_file(path_or_url: str) -> list:
    """
    Accept JSON (dict or list) or CSV.
    Returns list of rows: {code, label_en, label_fr}
    """
    text = Path(path_or_url).read_text(encoding='utf-8') if Path(path_or_url).exists() else None
    if text is None:
        # Should not happen because we materialize remote first
        return []
    # Try JSON
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            rows = []
            for code, val in obj.items():
                if isinstance(val, dict):
                    rows.append({
                        'code': code,
                        'label_en': val.get('en') or '',
                        'label_fr': val.get('fr') or val.get('en') or ''
                    })
                else:
                    rows.append({'code': code, 'label_en': str(val), 'label_fr': str(val)})
            return rows
        elif isinstance(obj, list):
            rows = []
            for item in obj:
                if isinstance(item, dict):
                    code = item.get('code') or item.get('id')
                    if not code:
                        continue
                    en = item.get('en') or item.get('label_en') or item.get('label') or ''
                    fr = item.get('fr') or item.get('label_fr') or en
                    rows.append({'code': code, 'label_en': en, 'label_fr': fr})
            return rows
    except json.JSONDecodeError:
        pass
    # Fallback CSV
    rows = []
    reader = csv.reader(text.splitlines())
    headers = None
    for r in reader:
        if not r:
            continue
        if headers is None and any(h.lower() in ('code', 'en', 'fr', 'label') for h in r):
            headers = [h.lower() for h in r]
            continue
        if headers:
            row = dict(zip(headers, r))
            code = row.get('code') or row.get('id')
            if not code:
                continue
            en = row.get('en') or row.get('label') or ''
            fr = row.get('fr') or en
        else:
            code = r[0]
            en = r[1] if len(r) > 1 else ''
            fr = r[2] if len(r) > 2 else en
        rows.append({'code': code, 'label_en': en, 'label_fr': fr})
    return rows

def expand_sources(patterns):
    expanded = []
    for p in patterns:
        if re.match(r'^https?://', p):
            expanded.append(p)
        elif any(ch in p for ch in ['*', '?', '[']):
            expanded.extend(sorted(glob(p)))
        else:
            expanded.append(p)
    return expanded

def materialize_sources(source_list, local_dir="dictionaries"):
    realized = []
    for s in source_list:
        if re.match(r'^https?://', s):
            local = fetch_remote(s, Path(local_dir))
            realized.append(str(local))
        else:
            realized.append(s)
    return realized

###############################################################################
# Choice set management (global + inline)
###############################################################################

def register_global_choice_set(name, file_path, choice_sets, warnings):
    """
    If not present, create. If present and content hash differs, replace (last-write-wins) and warn.
    """
    rows = parse_choice_file(file_path)
    # Build temp values list
    temp_values = []
    for row in rows:
        temp_values.append({
            'code': row['code'],
            'label_en': row['label_en'],
            'label_fr': row['label_fr'],
            'minister_history': None,
            'minister_history_count': 0
        })

    temp_hash = hashlib.sha1(
        json.dumps(sorted(temp_values, key=lambda v: v['code']), ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    ).hexdigest()

    if name not in choice_sets:
        cs = ChoiceSet(name, file_path, is_global=True)
        for v in temp_values:
            cs.add_value(v)
        cs.compute_hash()
        choice_sets[name] = cs
        return cs, False
    # Already exists
    existing = choice_sets[name]
    if existing.content_hash != temp_hash:
        warnings.append(f"Global choice set '{name}' updated (hash {existing.content_hash[:7]} -> {temp_hash[:7]}) from {existing.origin} to {file_path}")
        # Replace values (keep field_ids)
        field_ids = existing.field_ids.copy()
        new_cs = ChoiceSet(name, file_path, is_global=True)
        new_cs.field_ids = field_ids
        for v in temp_values:
            new_cs.add_value(v)
        new_cs.compute_hash()
        choice_sets[name] = new_cs
        return new_cs, True
    else:
        # Hash same; just update origin if needed
        existing.origin = file_path
        return existing, False

def register_inline_choice_set(dataset_type, field_id, choices_obj, choice_sets):
    name = f"{dataset_type}__{field_id}"
    if name not in choice_sets:
        cs = ChoiceSet(name, 'inline', is_global=False)
        for code, val in choices_obj.items():
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
                cs.add_value({
                    'code': code,
                    'label_en': label_en,
                    'label_fr': label_fr,
                    'minister_history': mh_list if mh_list else None,
                    'minister_history_count': len(mh_list) if mh_list else 0
                })
            else:
                s = str(val)
                cs.add_value({
                    'code': code,
                    'label_en': s,
                    'label_fr': s,
                    'minister_history': None,
                    'minister_history_count': 0
                })
        cs.compute_hash()
        choice_sets[name] = cs
    return choice_sets[name]

###############################################################################
# Core processing
###############################################################################

def process_resource(resource, dataset_type, choice_sets, warnings):
    fields_out = []
    for f in resource.get('fields', []):
        field_id = f.get('id') or f.get('datastore_id')
        label = normalize_text_obj(f.get('label', field_id))
        desc = normalize_text_obj(f.get('description', ""))
        validation = normalize_text_obj(f.get('validation', ""))
        obligation = normalize_text_obj(f.get('obligation', ""))
        required = (obligation.get('en', '').lower().startswith('mandat')
                    or f.get('excel_required') is True)
        datastore_type = f.get('datastore_type', '')
        max_chars = f.get('max_chars')

        choice_set = None
        if f.get('choices_file'):
            stem = Path(urlparse(f['choices_file']).path).stem
            cs, replaced = register_global_choice_set(stem, f['choices_file'], choice_sets, warnings)
            cs.add_field(field_id)
            choice_set = cs
        elif f.get('choices'):
            cs = register_inline_choice_set(dataset_type, field_id, f['choices'], choice_sets)
            cs.add_field(field_id)
            choice_set = cs
        if f.get('choices') and f.get('choices_file'):
            warnings.append(f"Field {field_id}: both 'choices' and 'choices_file' present (schema forbids).")

        fields_out.append({
            'id': field_id,
            'label': label,
            'description': desc,
            'validation': validation if (validation['en'] or validation['fr']) else None,
            'required': required,
            'datastore_type': datastore_type,
            'max_chars': max_chars,
            'choice_set': choice_set
        })
    return fields_out

def write_choice_set_docs(choice_sets, out_dir: Path):
    choices_dir = out_dir / 'choices'
    choices_dir.mkdir(parents=True, exist_ok=True)
    for cs in sorted(choice_sets.values(), key=lambda c: (not c.is_global, c.name.lower())):
        filename = f"{cs.name}.md"
        cs.output_filename = filename
        p = choices_dir / filename
        with p.open('w', encoding='utf-8') as fh:
            fh.write(f"# Choice Set: {cs.name}\n\n")
            fh.write(f"**Origin:** {cs.origin}\n\n")
            fh.write(f"**Scope:** {'Global' if cs.is_global else 'Inline (dataset-scoped)'}\n\n")
            fh.write(f"**Fields Using This Set:** {', '.join(sorted(cs.field_ids))}\n\n")
            fh.write(f"**Values (n={cs.cardinality}):**\n\n")
            if cs.has_minister_history:
                fh.write("| Code | Label (EN) | Label (FR) | Minister History Count |\n")
                fh.write("|------|------------|------------|-----------------------|\n")
            else:
                fh.write("| Code | Label (EN) | Label (FR) |\n")
                fh.write("|------|------------|------------|\n")
            for v in cs.values:
                if cs.has_minister_history:
                    fh.write(f"| `{v['code']}` | {v['label_en']} | {v['label_fr']} | {v.get('minister_history_count', 0)} |\n")
                else:
                    fh.write(f"| `{v['code']}` | {v['label_en']} | {v['label_fr']} |\n")
            if cs.has_minister_history:
                fh.write("\n## Minister History Details\n\n")
                for v in cs.values:
                    if v.get('minister_history'):
                        fh.write(f"### Code `{v['code']}` – {v['label_en']} / {v['label_fr']}\n\n")
                        fh.write("| Seq | Minister (EN) | Minister (FR) | Start | End |\n")
                        fh.write("|-----|---------------|---------------|-------|-----|\n")
                        for i, mh in enumerate(v['minister_history'], start=1):
                            fh.write(f"| {i} | {mh['en']} | {mh['fr']} | {mh.get('start','') or ''} | {mh.get('end','') or ''} |\n")
            fh.write("\n*Auto-generated choice set document.*\n")

    # Index
    with (choices_dir / 'index.md').open('w', encoding='utf-8') as idx:
        idx.write("# Choice Sets Index\n\n")
        idx.write("| Choice Set | Scope | Values | Fields | Doc | Minister History |\n")
        idx.write("|------------|-------|--------|--------|-----|------------------|\n")
        for cs in sorted(choice_sets.values(), key=lambda c: cs.name.lower()):
            idx.write(f"| {cs.name} | {'Global' if cs.is_global else 'Inline'} | {cs.cardinality} | {', '.join(sorted(cs.field_ids))} | {cs.output_filename} | {'Yes' if cs.has_minister_history else 'No'} |\n")

###############################################################################
# Rendering dataset docs
###############################################################################

def render_dataset_doc(dataset_json_path, data, validator, schema_obj, choice_sets, warnings, out_dir: Path, env):
    dataset_type = data.get('dataset_type')
    filename = f"{dataset_type}.md" if dataset_type else f"dict_{hashlib.sha1(dataset_json_path.encode()).hexdigest()[:8]}.md"

    schema_passed = True
    schema_warnings = []
    if schema_obj:
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            schema_passed = False
            for e in errors[:50]:
                schema_warnings.append(f"Schema error at {'/'.join(map(str, e.path)) or '<root>'}: {e.message}")

    resources_out = []
    for r in data.get('resources', []):
        r_title = normalize_text_obj(r.get('title', dataset_type))
        fields = process_resource(r, dataset_type, choice_sets, warnings)
        anchor = re.sub(r'[^a-z0-9]+', '-', r_title['en'].lower()).strip('-')
        resources_out.append({
            'title': r_title,
            'fields': fields,
            'anchor': anchor
        })

    # Build context of all choice sets referenced by this dataset (subset)
    referenced_names = set()
    for res in resources_out:
        for f in res['fields']:
            if f['choice_set']:
                referenced_names.add(f['choice_set'].name)

    all_choice_sets_context = []
    for name in sorted(referenced_names):
        cs = choice_sets[name]
        all_choice_sets_context.append({
            'name': cs.name,
            'fields': sorted(cs.field_ids),
            'cardinality': cs.cardinality,
            'output_filename': f"choices/{cs.output_filename}" if hasattr(cs, 'output_filename') else ''
        })

    tmpl = env.get_template('template.md.j2')
    context = {
        'dataset_type': dataset_type,
        'title': normalize_text_obj(data.get('title', dataset_type)),
        'notes': normalize_text_obj(data.get('notes', "")),
        'resources': resources_out,
        'all_choice_sets': all_choice_sets_context,
        'generation': {
            'timestamp_iso': datetime.datetime.utcnow().replace(microsecond=0).isoformat(),
            'source_display': dataset_json_path,
            'commit': git_commit(),
            'tool_version': TOOL_VERSION
        },
        'validation': {
            'passed': schema_passed,
            'warnings': schema_warnings + warnings  # combine
        }
    }
    rendered = tmpl.render(**context)
    (out_dir / filename).write_text(rendered, encoding='utf-8')
    return schema_passed

###############################################################################
# CLI
###############################################################################

@click.command()
@click.option('--source', '-s', multiple=True, required=True,
              help="Path, glob, or URL to recombinant JSON (repeatable).")
@click.option('--schema', default='schema/recombinant-schema.json',
              help="Path to validation schema.")
@click.option('--out-dir', default='docs/reference', show_default=True,
              help="Directory for generated markdown.")
@click.option('--fail-on-error/--no-fail-on-error', default=True,
              help="Exit non-zero if any dataset fails schema validation.")
def main(source, schema, out_dir, fail_on_error):
    # Expand and materialize sources
    expanded = expand_sources(source)
    local_sources = materialize_sources(expanded, local_dir="dictionaries")

    # Schema validator
    schema_obj = None
    validator = None
    if Path(schema).exists():
        schema_obj = json.loads(Path(schema).read_text(encoding='utf-8'))
        validator = Draft7Validator(schema_obj)

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)))

    # Shared choice sets across all datasets in this run
    global_choice_sets = {}

    overall_failures = 0
    dataset_warnings = []

    # First pass: load all data to allow last-write-wins semantics while preserving order
    datasets = []
    for src in local_sources:
        data, display = load_json(src)
        datasets.append((display, data))

    # Process each dataset
    for display, data in datasets:
        passed = render_dataset_doc(
            dataset_json_path=display,
            data=data,
            validator=validator,
            schema_obj=schema_obj,
            choice_sets=global_choice_sets,
            warnings=dataset_warnings,
            out_dir=out_path,
            env=env
        )
        if not passed:
            overall_failures += 1

    # After all datasets, write the master choice set docs (global + inline) once
    write_choice_set_docs(global_choice_sets, out_path)

    # Optional: could write a consolidated warning file
    if dataset_warnings:
        (out_path / "generation-warnings.log").write_text(
            "\n".join(dataset_warnings), encoding='utf-8'
        )

    if overall_failures and fail_on_error:
        click.echo(f"{overall_failures} dataset(s) failed validation.", err=True)
        sys.exit(1)

    click.echo(f"Completed: {len(datasets)} dataset(s); {len(global_choice_sets)} total choice set(s).")

if __name__ == '__main__':
    main()
