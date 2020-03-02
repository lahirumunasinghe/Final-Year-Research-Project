from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os



 ######################write data into csv file#####################
def writetoFile(lbp,harlick,gabor,glcm,label):
    filename = '/home/lahiru/Documents/FYP Madushini/finalMadushini.csv'
    file_exists = os.path.isfile(filename)
    print(file_exists)
    with open('/home/lahiru/Documents/FYP Madushini/finalMadushini.csv', mode='a') as csv_file:
       
        fieldnames = ['LBP1', 'LBP2', 'LBP3', 'LBP4', 'LBP5', 'LBP6', 'LBP7', 'LBP8', 'LBP9', 'LBP10', 'LBP11','LBP12', 'LBP13', 'LBP14', 'LBP15', 'LBP16', 'LBP17', 'LBP18', 'LBP19', 'LBP20', 'LBP21', 'LBP22', 'LBP23', 'LBP24', 'LBP25','LBP26','Harlick1', 'Harlick2','Harlick3','Harlick4','Harlick5','Harlick6','Harlick7','Harlick8','Harlick9','Harlick10','Harlick11','Harlick12','Harlick13','GaborEnergy','GaborEntropy','GLCMcontrast','GLCMdissimilarity','GLCMhomogeneity','GLCMenergy','GLCMcorrelation','Label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {'LBP1': lbp[0], 'LBP2': lbp[1], 'LBP3': lbp[2], 'LBP4': lbp[3], 'LBP5': lbp[4], 'LBP6': lbp[5], 'LBP7': lbp[6], 'LBP8': lbp[7], 'LBP9': lbp[8], 'LBP10': lbp[9], 'LBP11': lbp[10],'LBP12': lbp[11], 'LBP13': lbp[12], 'LBP14': lbp[13], 'LBP15': lbp[14], 'LBP16': lbp[15], 'LBP17': lbp[16], 'LBP18': lbp[17], 'LBP19': lbp[18], 'LBP20': lbp[19], 'LBP21': lbp[20], 'LBP22': lbp[21], 'LBP23': lbp[22], 'LBP24': lbp[23], 'LBP25': lbp[24],'LBP26': lbp[25],'Harlick1': harlick[0], 'Harlick2': harlick[1],'Harlick3': harlick[2],'Harlick4': harlick[3],'Harlick5': harlick[4],'Harlick6': harlick[5],'Harlick7': harlick[6],'Harlick8': harlick[7],'Harlick9': harlick[8],'Harlick10': harlick[9],'Harlick11': harlick[10],'Harlick12': harlick[11],'Harlick13': harlick[12],'GaborEnergy': gabor[0],'GaborEntropy': gabor[1],'GLCMcontrast': glcm[0],'GLCMdissimilarity': glcm[1],'GLCMhomogeneity': glcm[2],'GLCMenergy': glcm[3],'GLCMcorrelation': glcm[4],'Label': label})


