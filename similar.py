import dBspot
import sparql
import syn

def get_similar(synonyms,ontology):
    onto=list()
    for s in synonyms:
        for o in ontology:
            #print str(s)+'---------'+str(o)
            if str(s).lower() in str(o).lower():
                onto.append(o)
    return onto

def get_ever():
    print '--------------EVERYTHING--------------------'
    res=dBspot.get_res("What is the Population of China?")
    print 'resources  are ='+str(res)
    syno=syn.get_syn("Location")
    print '--------------Synonyms--------------------'
    print syno
    onto=sparql.get_onto(res[0])
    print '--------------Ontology--------------------'
    print onto
    syno=["Population"]
    print '--------------SIMILAR ONTOLOGIES--------------------'
    onto=get_similar(syno,onto)
    print onto
    print '--------------ONTOLOGIES LINKS--------------------'
    links=sparql.get_spec_onto(res[0],onto)
    for link in links:
        print link


get_ever()
