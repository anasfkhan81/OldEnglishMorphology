import argparse
from pathlib import Path
from pyoxigraph import Store, RdfFormat

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('query', type=Path)
parser.add_argument('--rdf', type=Path, default=ROOT/'rdf/oe_comparison.ttl')
args = parser.parse_args()
store = Store()
store.load(path=args.rdf, format=RdfFormat.TURTLE)
results = store.query(args.query.read_text(encoding='utf-8'))
print('\t'.join(v.value for v in results.variables))
for row in results:
    print('\t'.join(str(v) if v is not None else '' for v in row))
