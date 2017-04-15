import CoarseClassifier
import pickle
import os
from sklearn import svm
from sklearn import metrics
trainfile='train_5500.label'
testfile='TREC_10test.label'
def test():

    trainX, trainCY, testX, testCY, predictedCY, trainFY, testFY=CoarseClassifier.CoarseClassify(trainfile,testfile)
    classes=list(set(trainCY))
    traindatasetsX=dict()
    traindatasetsY=dict()
    testdatasetsX=dict()
    testdatasetsY=dict()
    for cls in classes:
        traindatasetsX[cls]=list()
        traindatasetsY[cls]=list()
        testdatasetsX[cls]=list()
        testdatasetsY[cls]=list()
    for idx,CC in enumerate(trainCY):
        traindatasetsX[CC].append(trainX[idx])
        traindatasetsY[CC].append(trainFY[idx])
    for idx,CC in enumerate(testCY):
        testdatasetsX[CC].append(testX[idx])
        testdatasetsY[CC].append(testFY[idx])
    for cls in classes:
        classify(traindatasetsX[cls],traindatasetsY[cls],testdatasetsX[cls],testdatasetsY[cls],cls)

def predict(CourseClass,testX,trainX,trainCY,trainFY):
    #trainX, trainCY, trash, testCY, predictedCY, trainFY, testFY = CoarseClassifier.CoarseClassify(trainfile, testfile)
    classes = list(set(trainCY))
    traindatasetsX = dict()
    traindatasetsY = dict()
    for cls in classes:
        traindatasetsX[cls] = list()
        traindatasetsY[cls] = list()
    for idx, CC in enumerate(trainCY):
        traindatasetsX[CC].append(trainX[idx])
        traindatasetsY[CC].append(trainFY[idx])
    return singularclassify(traindatasetsX[CourseClass], traindatasetsY[CourseClass], testX, CourseClass)

def singularclassify(trainX, trainY,testX,cls):
    filename = str(cls)+'.pkl'
    if os.path.isfile(filename):
        model = pickle.load(open(filename, 'rb'))
    else:
        model = svm.SVC(decision_function_shape='ovo', verbose=True)
        model.fit(trainX, trainY)
        pickle.dump(model, open(filename, 'wb'))
    predicted = model.predict(testX)
    return predicted
def text(str):
    #str="Modi"
    predicted,strX,trainX,trainCY,trainFY=CoarseClassifier.CoarseClassifytext(trainfile,str)
    CC=predicted[0]
    FC = predict(CC,strX,trainX,trainCY,trainFY)[0]
    print CC,FC
    return CC,FC

def classify(trainX, trainY, testX, testY,cls):
    filename = str(cls)+'.pkl'
    if os.path.isfile(filename):
        model = pickle.load(open(filename, 'rb'))
    else:
        model = svm.SVC(decision_function_shape='ovo', verbose=True)
        model.fit(trainX, trainY)
        pickle.dump(model, open(filename, 'wb'))
    predicted = model.predict(testX)
    accuracy = metrics.accuracy_score(testY, predicted)
    print cls
    print accuracy
    print metrics.confusion_matrix(testY, predicted)

def main():
    t=raw_input("Enter Question")
    text(t)
if __name__ == '__main__':
    main()