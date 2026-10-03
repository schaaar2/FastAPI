from rdflib import Graph
 
g = Graph()
g.parse("ontology/usdm.ttl")
 
print(f"Triples: {len(g)}")
