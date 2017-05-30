import nltk
import pandas as pd
from sklearn import svm
import csv
from sklearn.feature_extraction.text import CountVectorizer

def getstopwords():
    temp=pd.read_csv('stopwords',header=None)
    a=temp.values.tolist()
    temp=list(zip(*a)[0])
    temp.append(" ")
    temp.append("")
    temp.append("` `")
    temp.append("?")
    temp.append("'s")
    temp.append("~")
    return temp
def getdataframe(filename):
    return pd.read_csv(filename,header=None,delimiter='\n')
def getnonstopwords(words,stopwords):
    nonstopwords = [word for word in words if word.lower() not in stopwords]

    return nonstopwords
def column(matrix, i):
    return [row[i] for row in matrix]

def preprocess(dataframe):
    #attr=['Qno.','word','FClass','CClass']
    dataset=list()
    #dataset.append(attr)

    vectorizer = CountVectorizer(min_df=1,decode_error='ignore')
    for Qid in range(dataframe.shape[0]):
        splits=dataframe.loc[Qid][0].split()
        cc,fc=splits[0].split(":")
        words=splits[1:]
        nonstopwords=getnonstopwords(words,getstopwords())
        temp = list()
        temp.append(Qid)
        temp.append(" ".join(nonstopwords))
        temp.append(fc)
        temp.append(cc)
        dataset.append(temp)
    X=column(dataset,1)
    # X = vectorizer.fit_transform(X)
    # X=X.toarray()
    # Xdf=pd.DataFrame(data=X,index=None,columns=vectorizer.get_feature_names())
    FY=column(dataset,-2)
    CY=column(dataset,-1)
    # attri=vectorizer.get_feature_names()
    return X,FY,CY

def getdataset(filename):
    return preprocess(getdataframe(filename))

def main():
    stopwords=getstopwords()
    dataset = preprocess(getdataframe('train_5500.label'))

if __name__ == '__main__':
    main()
