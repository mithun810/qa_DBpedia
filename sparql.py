from SPARQLWrapper import SPARQLWrapper, JSON
import dBspot
import cos_sim

def get_onto(res):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        SELECT ?Property?h WHERE
    {
    <http://dbpedia.org/resource/"""+res+"""> ?Property?h .
    }
    """)
    prop=list()
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results['results']['bindings']:
        res=result['Property']['value']
        if 'ontology' in str(res):
            prop.append(res.split("ontology/")[1])
    return prop

def get_spec_onto(res,ontos):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        SELECT ?Property?h WHERE
    {
    <http://dbpedia.org/resource/"""+res+"""> ?Property?h .
    }
    """)
    prop=list()
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for o in ontos:
        for result in results['results']['bindings']:
            resu=result['Property']['value']
            if str(o) in str(resu):
                prop.append(resu)
    return prop
print get_onto("China")
