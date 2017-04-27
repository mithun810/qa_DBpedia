import dBspot
import sparql
import syn
from SPARQLWrapper import SPARQLWrapper, JSON

def get_abstract(res):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    abstract=list()
    sparql.setQuery("""
        SELECT ?value WHERE
    {
    <http://dbpedia.org/resource/"""+res+""">
    <http://dbpedia.org/ontology/abstract> ?value .
     filter (lang(?value)="en")
    }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results['results']['bindings']:
        return result['value']['value']


def final(res,onto_links):
    value=list()
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    for ol in onto_links:
        sparql.setQuery("""
            SELECT ?value WHERE
        {
        <http://dbpedia.org/resource/"""+res+""">

        <"""+ol+"""> ?value .
        }
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results['results']['bindings']:
            ress=result['value']['value']
            value.append(ress)
    set(value)
    print "===================-------------------FINAL ANSWER------------------========================"
    print set(value)
    '''for v in set(value):
        if "resource" in v:
            print get_abstract(res)
            return null
        else :
            print v
            return'''


def get_similar(synon,ontology):
    ontoo=list()
    print 'debug+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    print synon
    for s in synon:
        for o in ontology:
            if str(s).lower() in str(o).lower():
                ontoo.append(o)
                print "inside"

    return ontoo

def get_ever(query):
    synonym=list()
    #query="China speaks what language" #NO Need of ? We append Automaticlly :P
    print '==========================--------------EVERYTHING-------------=================================='
    res=dBspot.get_res(query)
    print 'resources  are ='+str(res)
    '''for w in query.split(" "):
        if res[0] not in w:
            syno=syn.get_syn(w)'''
    synonym=syn.get_syn("Location")
    print '===========================--------------Synonyms----------------================================'
    print synonym
    onto=sparql.get_onto(res[0])
    print '===========================--------------Ontology-----------------================================'
    print onto
    syno=["leader"]
    print '===========================------------SIMILAR ONTOLOGIES-----------================================'
    sim_onto=get_similar(syno,onto)
    print sim_onto
    print '============================------------ONTOLOGIES LINKS-----------================================'
    links=sparql.get_spec_onto(res[0],sim_onto)
    onto_links=list()
    for link in links:
        onto_links.append(link)
    print set(onto_links)

    final(res[0],set(onto_links))
query = raw_input("Enter Question \n")
get_ever(query)
