import resizeImage as ri
import glob
import cv2
import os
import pickle
import distanceMeasuringEdit as dm
from sklearn.preprocessing import StandardScaler
import CsvFileWrite as cw
import pandas as pd
import time


def ExtractFetureForSVM(path):
    print (path)
    filenames =path
    filenames.sort()
    images = [cv2.imread(img) for img in filenames]
    arrImg = [] # details of array
    ImgN = 0;

    for sample in images:
        arrImg.append([])
        median,mode,mean =dm.measureDistance(sample)
        arrImg[ImgN].append(median)
        arrImg[ImgN].append(mode)
        arrImg[ImgN].append(mean)
        ImgN = ImgN+1

    cw.writetoFile(arrImg)

def runMain(path):

    #print (path)
    ri.imSlice(path)

    path2 = glob.glob("/home/lahiru/PycharmProjects/untitled/SliceImage/*.png")
    time.sleep(1)
    ExtractFetureForSVM(path2)

    # Loading dataset and view a few records.
    dataset = pd.read_csv('/home/lahiru/PycharmProjects/untitled/finalLahiruTrain.csv')
    test = pd.read_csv('/home/lahiru/PycharmProjects/untitled/finalLahiruTemp.csv')

    attributes = list(dataset.columns[:27])
    X = dataset[attributes].values
    sc = StandardScaler()
    X = sc.fit(X)
    test = test[attributes].values
    test = sc.transform(test)

    filename = 'finalized_modelLahiru.sav'

    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    Y_Pred = loaded_model.predict(test)

    #os.remove('/home/lahiru/PycharmProjects/untitled/finalLahiruTemp.csv')

    print (Y_Pred)

    if Y_Pred==0:
        print("Benign nodule")
    else:
        print("Malignant nodule")


pathRead ='/home/lahiru/PycharmProjects/untitled/malignant/5.jpg'
runMain(pathRead)
