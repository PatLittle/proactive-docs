#!/usr/bin/env python3
import json
import csv
import urllib.request
from pathlib import Path
from datetime import datetime

URLS_FILE = 'recombinant-published-schema-urls.txt'
DICTS_DIR = 'dictionaries'
CKAN_DIR = 'ckan_schemas'
CHOICES_DIR = 'docs/choices'


def fetch_url(url, dest_dir):
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = Path(url.split('?')[0]).name
    if not name.endswith('.json'):
        name += '.json'
    dest = dest_dir / name
    with urllib.request.urlopen(url) as r:
        dest.write_bytes(r.read())
    return dest


def parse_choices(field):
    if 'choices' in field:
        rows = []
        for code, val in field['choices'].items():
            if isinstance(val, dict):
                en = val.get('en', '')
                fr = val.get('fr', en)
                extra = {k: v for k, v in val.items() if k not in ('en', 'fr')}
            else:
                en = fr = str(val)
                extra = {}
            rows.append({'code': code, 'en': en, 'fr': fr, 'extra': extra})
        return rows
    if 'choices_file' in field:
        url = field['choices_file']
        with urllib.request.urlopen(url) as r:
            text = r.read().decode('utf-8')
        reader = csv.reader(text.splitlines())
        rows = []
        header = None
        for row in reader:
            if not row:
                continue
            if header is None and any(h.lower() in ('code', 'en', 'fr') for h in row):
                header = [h.lower() for h in row]
                continue
            if header:
                data = dict(zip(header, row))
                rows.append({'code': data.get('code'), 'en': data.get('en') or '', 'fr': data.get('fr') or data.get('en') or '', 'extra': {}})
            else:
                code = row[0]
                en = row[1] if len(row) > 1 else ''
                fr = row[2] if len(row) > 2 else en
                rows.append({'code': code, 'en': en, 'fr': fr, 'extra': {}})
        return rows
    return []


def add_choice(storage, field_id, code, en, fr, extra, doc):
    """Add a choice value and reference to the storage dict."""
    entry = storage.setdefault(field_id, {"values": {}, "references": set()})
    entry["values"][code] = {"en": en, "fr": fr, "extra": extra}
    if doc:
        entry["references"].add(doc)


def main():
    urls = [u.strip() for u in Path(URLS_FILE).read_text().splitlines() if u.strip()]
    CHOICES_PATH = Path(CHOICES_DIR)
    CHOICES_PATH.mkdir(parents=True, exist_ok=True)
    all_choices = {}
    generated_files = set()
    generated_dicts = set()
    for url in urls:
        local = fetch_url(url, Path(DICTS_DIR))
        generated_dicts.add(local.name)
        data = json.loads(local.read_text(encoding='utf-8'))
        dataset_type = data.get('dataset_type', Path(local).stem)
        doc_ref = f'reference/{dataset_type}.md'
        for res in data.get('resources', []):
            for f in res.get('fields', []):
                values = parse_choices(f)
                if not values:
                    continue
                field_id = f['id']
                for v in values:
                    add_choice(all_choices, field_id, v['code'], v['en'], v['fr'], v.get('extra', {}), doc_ref)

    # Parse CKAN schemas for choice references
    for path in Path(CKAN_DIR).glob('*.json'):
        data = json.loads(path.read_text(encoding='utf-8'))
        doc_ref = f'ckan/{path.stem}.md'
        fields = []
        fields.extend(data.get('dataset_fields', []))
        fields.extend(data.get('resource_fields', []))
        fields.extend(data.get('fields', []))
        for f in fields:
            choices = f.get('choices')
            if not isinstance(choices, list) or not choices:
                continue
            field_id = f.get('field_name')
            if not field_id:
                continue
            for ch in choices:
                code = ch.get('value')
                label = ch.get('label')
                if isinstance(label, dict):
                    en = label.get('en', '')
                    fr = label.get('fr', '')
                else:
                    en = fr = str(label) if label is not None else str(code)
                add_choice(all_choices, field_id, code, en, fr, {}, doc_ref)
    timestamp = datetime.utcnow().isoformat(timespec='seconds')
    for field_id, data in all_choices.items():
        path = CHOICES_PATH / f"{field_id}.md"
        generated_files.add(path.name)
        lines = [
            f"# Choices for {field_id}",
            '',
            f"Generated {timestamp} UTC",
            '',
            '| Code | Label (EN) | Label (FR) |',
            '|------|------------|------------|',
        ]
        for code, val in sorted(data['values'].items()):
            link = f"[`{code}`](#{code})" if val.get('extra') else f"`{code}`"
            lines.append(f"| {link} | {val['en']} | {val['fr']} |")
        lines.append('')
        for code, val in sorted(data['values'].items()):
            extra = val.get('extra')
            if not extra:
                continue
            en = val['en']
            fr = val['fr']
            lines.append(f"### Code `{code}` – {en} / {fr} {{#{code}}}")
            lines.append('')
            if isinstance(extra, dict) and 'ministers' in extra and isinstance(extra['ministers'], list):
                lines.append('| Row | Minister (EN) | Minister (FR) | Start | End |')
                lines.append('|-----|---------------|---------------|-------|-----|')
                for i, m in enumerate(extra['ministers'], 1):
                    en_name = m.get('name_en') or m.get('name', '')
                    fr_name = m.get('name_fr') or en_name
                    start = m.get('start_date', '')
                    end = m.get('end_date', '')
                    lines.append(f"| {i} | {en_name} | {fr_name} | {start} | {end} |")
                leftover = {k: v for k, v in extra.items() if k != 'ministers'}
                if leftover:
                    lines.append('')
                    lines.append('| Key | Value |')
                    lines.append('|-----|-------|')
                    for k, v in leftover.items():
                        if isinstance(v, (dict, list)):
                            val_str = json.dumps(v, ensure_ascii=False)
                        else:
                            val_str = str(v)
                        lines.append(f"| {k} | {val_str} |")
            else:
                lines.append('| Key | Value |')
                lines.append('|-----|-------|')
                for k, v in extra.items():
                    if isinstance(v, (dict, list)):
                        val_str = json.dumps(v, ensure_ascii=False)
                    else:
                        val_str = str(v)
                    lines.append(f"| {k} | {val_str} |")
            lines.append('')
        if data['references']:
            lines.append('')
            lines.append('## Referenced By')
            lines.append('')
            for ref in sorted(data['references']):
                lines.append(f'- [{ref}](../{ref})')
            lines.append('')
        path.write_text("\n".join(lines), encoding='utf-8')

    # remove docs no longer referenced
    for f in CHOICES_PATH.glob('*.md'):
        if f.name not in generated_files:
            f.unlink()

    # remove dictionaries no longer referenced
    dicts_path = Path(DICTS_DIR)
    for f in dicts_path.glob('*.json'):
        if f.name not in generated_dicts:
            f.unlink()


if __name__ == '__main__':
    main()
