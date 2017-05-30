import pandas as pd
from sklearn import svm
from sklearn import metrics
import Preprocessor
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
def split(dataset):
    return dataset[:][:len(dataset[0])-1],dataset[:][-1]

def classify(trainX,trainY,testX,testY,trainFY,testFY):
    filename='cclassify.pkl'
    if os.path.isfile(filename):
        model1=pickle.load(open(filename,'rb'))
        model=model1
    else:
        model = svm.SVC(decision_function_shape='ovo', verbose=True)
        model.fit(trainX,trainY)
        pickle.dump(model,open(filename,'wb'))
    predicted=model.predict(testX)
    accuracy=metrics.accuracy_score(testY,predicted)

    print accuracy
    print metrics.confusion_matrix(testY,predicted)
    return trainX,trainY,testX,testY,predicted,trainFY,testFY

def predict(testX):
    filename='cclassify.pkl'
    if os.path.isfile(filename):
        model=pickle.load(open(filename,'rb'))
        predicted = model.predict(testX)
        return predicted
    else:
        print "First train then pass text"
        exit(0)
    pass


def CoarseClassify(trainfile,testfile):
    fulltrainX,fulltrainFY,fulltrainCY=Preprocessor.getdataset(trainfile)
    fulltestX,fulltestFY,fulltestCY=Preprocessor.getdataset(testfile)
    vec = TfidfVectorizer(binary=True, use_idf=True,decode_error='ignore')
    tfidf_train_data = vec.fit_transform(fulltrainX)
    tfidf_test_data = vec.transform(fulltestX)
    trainX=tfidf_train_data.toarray().tolist()
    testX=tfidf_test_data.toarray().tolist()
    return classify(trainX,fulltrainCY,testX,fulltestCY,fulltrainFY,fulltestFY)

def CoarseClassifyt(trainfile,text):
    process = "dummy:dummy " + text
    textdf = pd.DataFrame(data=[process])
    fulltrainX,fulltrainFY,fulltrainCY=Preprocessor.getdataset(trainfile)
    fulltestX,fulltestFY,fulltestCY=Preprocessor.preprocess(textdf)
    vec = TfidfVectorizer(binary=True, use_idf=True,decode_error='ignore')
    tfidf_train_data = vec.fit_transform(fulltrainX)
    tfidf_test_data = vec.transform(fulltestX)
    trainX=tfidf_train_data.toarray().tolist()
    testX=tfidf_test_data.toarray().tolist()
    return classify(trainX,fulltrainCY,testX,fulltestCY,fulltrainFY,fulltestFY)

def CoarseClassifytext(trainfile,text):
    process="dummy:dummy "+text
    textdf=pd.DataFrame(data=[process])
    fulltrainX,fulltrainFY,fulltrainCY=Preprocessor.getdataset(trainfile)
    fulltestX,Trash1,Trash2=Preprocessor.preprocess(textdf)
    vec = TfidfVectorizer(binary=True, use_idf=True, decode_error='ignore')
    tfidf_train_data = vec.fit_transform(fulltrainX)
    tfidf_test_data = vec.transform(fulltestX)
    trainX=tfidf_train_data.toarray().tolist()
    testX = tfidf_test_data.toarray().tolist()
    return predict(testX),testX,trainX,fulltrainCY,fulltrainFY
def main():
    CoarseClassify('train_5500.label','TREC_10test.label')
