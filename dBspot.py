import pycurl, json
import requests as req

def get_res(query):
    url = 'http://model.dbpedia-spotlight.org/en/annotate'
    data = {"text": query,"confidence":"0.35" ,"Subject": "Pycurl", "TextBody": "Some text"}
    headers = {"Accept" : "application/json"}
    res = req.get(url, params=data, headers=headers)
    #print res.content
    j=json.loads(res.content)
    for res in j["Resources"]:
        print res["@surfaceForm"]


get_res("Who is the king of Karnataka?")
