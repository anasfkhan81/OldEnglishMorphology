
from pathlib import Path
from pyRdfa import pyRdfa

pathin_1 ="data/clark_hall_rdfa_v1.xml" 
pathout_1 = "output/clark_hall_rdfa_v1.ttl"

pathin_2 = "data/sample.xml"
pathout_2 = "output/sample.ttl"

pathin_3 = "data/XML/CH_SV_failed_to_parse_rdfa.xml"
pathout_3 = "output/clark_hall_rdfa.ttl"

input_file = Path(pathin_3)  # Change this to pathin_1 or pathin_2 as needed
output_file = Path(pathout_3)

output_file.parent.mkdir(parents=True, exist_ok=True)

processor = pyRdfa(
    media_type="application/xml"
)

# Open the XML file directly rather than passing a file:/// URL
with input_file.open("rb") as xml_file:
    graph = processor.graph_from_source(xml_file)

graph.serialize(
    destination=str(output_file),
    format="turtle"
)

print(f"Extracted {len(graph)} RDF triples")
print(f"Saved to {output_file}")
