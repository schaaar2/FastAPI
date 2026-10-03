from rdflib import Graph
 
g = Graph()
g.parse("ontology/site_readiness_demo.ttl")
 
print(f"Triples: {len(g)}")
