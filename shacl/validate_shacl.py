from pathlib import Path
from pyshacl import validate

BASE = Path(__file__).resolve().parent

data_file = BASE / "clark_hall_strong_verb_classes_chm_ontology.ttl"
shapes_file = BASE / "clark_hall_shapes.ttl"

conforms, report_graph, report_text = validate(
    data_graph=str(data_file),
    shacl_graph=str(shapes_file),
    data_graph_format="turtle",
    shacl_graph_format="turtle",
    inference="none",
    advanced=True
)

print("Conforms:", conforms)
print(report_text)
