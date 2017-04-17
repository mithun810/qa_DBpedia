import pycurl, json
import requests as req
import FineClassifier
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree
import nltk
from nltk.chunk.regexp import RegexpChunkRule
from nltk.tokenize import PunktSentenceTokenizer
from nltk import RegexpParser

def get_res(query):
    url = 'http://model.dbpedia-spotlight.org/en/annotate'
    data = {"text": query,"confidence":"0.35" ,"Subject": "Pycurl", "TextBody": "Some text"}
    headers = {"Accept" : "application/json"}
    res = req.get(url, params=data, headers=headers)
    #print res.content
    reso=list()
    j=json.loads(res.content)
    for res in j["Resources"]:
        reso.append( res["@surfaceForm"])
    print reso
    return reso

def get_key(query):
    text=nltk.pos_tag(query.split())
    strr=""
    grammar = r"""
    Key:{<DT|PP\$>?<JJ.*>*<NN>|<NNP.*><\:><VBD>}
    """
    cp=RegexpParser(grammar)
    print cp.parse(text)
    #print text
    for t in text:
        for idx, w in enumerate(t):
            if idx==0:
                strr=strr+w+"/"
            else :
                strr=strr+w
        strr=strr+" "
    RegexpChunkRule.fromstring(r'''<DT>?}{<IN>+<NN.*>?''')
    chunked_text=tagstr2tree(strr)
    #print strr
    text =str(chunked_text)
    tree = nltk.Tree.fromstring(text, read_leaf=lambda x: x.split("/")[0])
    print(tree.leaves())
'''  tokenized=custom_sent_tokenizer.tokenize(query)
    try:
        for i in tokenized:
            words =nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkgram=r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>}

            """
            chunkparser=nltk.RegexpParser(chunkgram)
            chunked=chunkparser.parse(tagged)
            print chunked
    except Exception as e:
        print str(e)
'''


get_key("Presindent of India")
