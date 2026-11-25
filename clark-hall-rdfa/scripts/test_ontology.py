from rdflib import Graph

g = Graph()

g.parse(
    "data/clark_hall_strong_verb_classes_chm_ontology.ttl",
    format="turtle"
)

g.parse(
    "output/lacan.ttl",
    format="turtle"
)

query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX chm: <https://example.org/chm#>

SELECT DISTINCT ?lemma ?class
WHERE {
    ?verb rdf:type ?class ;
          ontolex:canonicalForm/ontolex:writtenRep ?lemma .

    ?class rdfs:subClassOf* chm:StrongVerbVII .
}
"""

for row in g.query(query):
    print(row.lemma, row["class"])