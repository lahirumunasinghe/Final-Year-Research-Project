from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os



 ######################write data into csv file#####################
def writetoFile(arrVal):
    filename = '/home/lahiru/PycharmProjects/untitled/finalLahiruTemp.csv'
    file_exists = os.path.isfile(filename)
    print(file_exists)
    with open('/home/lahiru/PycharmProjects/untitled/finalLahiruTemp.csv', mode='w') as csv_file:

        fieldnames = ['img1median','img1mode','img1mean','img2median','img2mode','img2mean','img3median','img3mode','img3mean','img4median','img4mode','img4mean','img5median','img5mode','img5mean',
                      'img6median','img6mode','img6mean','img7median','img7mode','img7mean','img8median','img8mode','img8mean','img9median','img9mode','img9mean'] #has to make the csv file
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {'img1median': arrVal[0][0], 'img1mode': arrVal[0][1], 'img1mean': arrVal[0][2], 'img2median': arrVal[1][0], 'img2mode': arrVal[1][1], 'img2mean': arrVal[1][2], 'img3median': arrVal[2][0], 'img3mode': arrVal[2][1], 'img3mean': arrVal[2][2],
             'img4median': arrVal[3][0], 'img4mode': arrVal[3][1], 'img4mean': arrVal[3][2], 'img5median': arrVal[4][0], 'img5mode': arrVal[4][1], 'img5mean': arrVal[4][2],'img6median': arrVal[5][0], 'img6mode': arrVal[5][1], 'img6mean': arrVal[5][2],
             'img7median': arrVal[6][0], 'img7mode': arrVal[6][1], 'img7mean': arrVal[6][2],'img8median': arrVal[7][0], 'img8mode': arrVal[7][1], 'img8mean': arrVal[7][2],'img9median': arrVal[8][0], 'img9mode': arrVal[8][1], 'img9mean': arrVal[8][2]})


def writetoFileForTrain(arrVal,label):
    filename = '/home/lahiru/PycharmProjects/untitled/finalLahiruTrain.csv'
    file_exists = os.path.isfile(filename)
    print(file_exists)
    with open('/home/lahiru/PycharmProjects/untitled/finalLahiruTrain.csv', mode='a') as csv_file:

        fieldnames = ['img1median','img1mode','img1mean','img2median','img2mode','img2mean','img3median','img3mode','img3mean','img4median','img4mode','img4mean','img5median','img5mode','img5mean',
                      'img6median','img6mode','img6mean','img7median','img7mode','img7mean','img8median','img8mode','img8mean','img9median','img9mode','img9mean','Label'] #has to make the csv file
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {'img1median': arrVal[0][0], 'img1mode': arrVal[0][1], 'img1mean': arrVal[0][2], 'img2median': arrVal[1][0], 'img2mode': arrVal[1][1], 'img2mean': arrVal[1][2], 'img3median': arrVal[2][0], 'img3mode': arrVal[2][1], 'img3mean': arrVal[2][2],
             'img4median': arrVal[3][0], 'img4mode': arrVal[3][1], 'img4mean': arrVal[3][2], 'img5median': arrVal[4][0], 'img5mode': arrVal[4][1], 'img5mean': arrVal[4][2],'img6median': arrVal[5][0], 'img6mode': arrVal[5][1], 'img6mean': arrVal[5][2],
             'img7median': arrVal[6][0], 'img7mode': arrVal[6][1], 'img7mean': arrVal[6][2],'img8median': arrVal[7][0], 'img8mode': arrVal[7][1], 'img8mean': arrVal[7][2],'img9median': arrVal[8][0], 'img9mode': arrVal[8][1], 'img9mean': arrVal[8][2],'Label':label})

