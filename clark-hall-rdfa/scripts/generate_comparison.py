import argparse
import csv
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = '''@prefix exentry: <https://example.org/ch/> .
@prefix ex: <https://example.org/source/> .
@prefix chm: <https://example.org/chm#> .
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
'''
CLASSES = {'I', 'II', 'III', 'IV', 'V', 'VI', 'VII'}

def literal(value):
    return json.dumps(value, ensure_ascii=False)

def generate(source, output):
    entries = {}
    with source.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        required = {'Lemma', 'CH ID', 'CH', 'Arista', 'Arista Class'}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f'Missing columns: {required - set(reader.fieldnames or [])}')
        for row in reader:
            if not any(row.values()):
                continue
            def get(key):
                return (row.get(key) or '').strip()
            ident = get('CH ID')
            if not re.fullmatch(r'CAS2\.[A-Za-z0-9_.-]+', ident) or ident.endswith('.'):
                raise ValueError(f'Line {reader.line_num}: invalid CH ID {ident!r}')
            labels, claims = entries.setdefault(ident, (set(), defaultdict(set)))
            if get('Lemma'):
                labels.add(get('Lemma'))
            for col, src in [('Lemma', 'ClarkHall'), ('Arista', 'Arista')]:
                if get(col):
                    claims['chm:headword', literal(get(col))].add(src)
            for col, src in [('CH', 'ClarkHall'), ('Arista Class', 'Arista')]:
                value = get(col)
                if not value:
                    continue
                for cls in (part.strip() for part in value.split(',')):
                    if cls not in CLASSES:
                        raise ValueError(f'Line {reader.line_num}: unsupported class {cls!r} in {col} (cell: {value!r})')
                    claims['rdf:type', 'chm:StrongVerb' + cls].add(src)
    lines = [PREFIXES]
    for ident, (labels, claims) in entries.items():
        entry = f'exentry:{ident}_entry'
        lines.append(f'{entry} a ontolex:LexicalEntry .')
        for label in sorted(labels):
            lines.append(f'{entry} rdfs:label {literal(label)}@ang .')
        for (predicate, obj), sources in claims.items():
            sources = ', '.join('ex:' + s for s in sorted(sources))
            lines.append(f'<< {entry} {predicate} {obj} >>\n    dcterms:source {sources} .')
        lines.append('')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {len(entries)} entries to {output}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=ROOT/'data/strong_verb_comparison.tsv')
    parser.add_argument('--output', type=Path, default=ROOT/'rdf/oe_comparison.ttl')
    args = parser.parse_args()
    generate(args.input, args.output)
