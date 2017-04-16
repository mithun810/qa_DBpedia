import requests
import re
from xml.etree import ElementTree as ET
import json, xmljson
from lxml.etree import fromstring, tostring
def get_syn(word):
    #url='http://www.stands4.com/services/v2/syno.php?uid=5692&tokenid=tothzz2uvdRIlkB0&word='+words
    urlw='http://www.dictionaryapi.com/api/v1/references/ithesaurus/xml/'+word+'?key=771d82df-7d85-4897-b2e7-5a567a028a1f'
    #http://www.dictionaryapi.com/api/v1/references/ithesaurus/xml/Population?key=771d82df-7d85-4897-b2e7-5a567a028a1f
    r = requests.get(urlw)
    #print ''+r.content
    tree=ET.fromstring(r.content)
    synonyms=''
    itr=tree.iter('syn')
    for i in itr:
        synonyms = synonyms+" "+i.text
    if synonyms == '':
        itr = tree.iter('suggestion')
        for i in itr:
            synonyms = synonyms+" "+i.text
    return re.split(r'[, ]', synonyms)
    # #print xml[0]
    # js=json.dumps(xmljson.badgerfish.data(xml))
    # jsonstr=json.loads(''+js)
    # #print jsonstr
    # p= jsonstr['entry_list']['entry']['senprints']['syn']['$']
    # return p.split(', ')
if __name__ == '__main__':
    text = raw_input("Enter word ")
    print get_syn(text)


