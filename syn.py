import requests

from xml.etree import ElementTree
import json, xmljson
from lxml.etree import fromstring, tostring

r = requests.get('http://www.dictionaryapi.com/api/v1/references/ithesaurus/xml/umpire?key=771d82df-7d85-4897-b2e7-5a567a028a1f')
print ''+r.content
xml=fromstring(''+r.content)
js=json.dumps(xmljson.badgerfish.data(xml))
print js
