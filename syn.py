import requests

from xml.etree import ElementTree
import json, xmljson
from lxml.etree import fromstring, tostring
def get_syn(word):
    url='http://www.stands4.com/services/v2/syno.php?uid=5692&tokenid=tothzz2uvdRIlkB0&word=location'
    urlw='http://www.dictionaryapi.com/api/v1/references/ithesaurus/xml/'+word+'?key=771d82df-7d85-4897-b2e7-5a567a028a1f'
    r = requests.get(urlw)
    #print ''+r.content
    xml=fromstring(''+r.content)
    #print xml[0]
    js=json.dumps(xmljson.badgerfish.data(xml))
    jsonstr=json.loads(''+js)
    #print jsonstr
    p= jsonstr['entry_list']['entry']['sens']['syn']['$']
    return p.split(', ')

print get_syn("Location")
