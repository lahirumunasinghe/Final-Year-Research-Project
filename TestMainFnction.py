import resizeImage as ri
import glob
import cv2
import time
import os
import pickle
import distanceMeasuringEdit as dm
from sklearn.preprocessing import StandardScaler
import CsvFileWrite as cw
import pandas as pd
from matplotlib import pyplot as plt

# def ExtractFetureForSVM(path):
#     filenames =path
#     filenames.sort()
#     images = [cv2.imread(img) for img in filenames]
#     arrImg = [] # details of array
#     ImgN = 0;
#
#     for sample in images:
#         arrImg.append([])
#         median,mode,mean =dm.measureDistance(sample)
#         arrImg[ImgN].append(median)
#         arrImg[ImgN].append(mode)
#         arrImg[ImgN].append(mean)
#         ImgN = ImgN+1
#
#     cw.writetoFile(arrImg)

def viewImage(image):
    plt.imshow(image)
    plt.show()


def ExtractFetureForSVMTrain(path,val):

    filenames =path
    filenames.sort()
    images = [cv2.imread(img) for img in filenames]
    arrImg = [] # details of array
    ImgN = 0;

    for sample in images:
        # viewImage(sample)
        arrImg.append([])
        median,mode,mean =dm.measureDistance(sample)
        arrImg[ImgN].append(median)
        arrImg[ImgN].append(mode)
        arrImg[ImgN].append(mean)
        ImgN = ImgN+1


    cw.writetoFileForTrain(arrImg,val)


def ExtractFetureWithNotSepSVM(path,val):
    # print (path)
    filenames =path
    filenames.sort()
    #images = for img in filenames]

    for sample in filenames:
        #viewImage(cv2.imread(sample))
        ri.imSlice(sample)
        time.sleep(1)
        path2 = glob.glob('/home/lahiru/PycharmProjects/untitled/SliceImage/*.png')
        ExtractFetureForSVMTrain(path2,val)


path1 = glob.glob('/home/lahiru/PycharmProjects/untitled/benign/*.jpg')
path2 = glob.glob('/home/lahiru/PycharmProjects/untitled/malignant/*.jpg')

ExtractFetureWithNotSepSVM(path1,0)
ExtractFetureWithNotSepSVM(path2,1)
