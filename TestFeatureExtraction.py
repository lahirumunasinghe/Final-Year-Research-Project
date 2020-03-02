import PIL
# from harlick import extract_features
from LBPFeatures import desc
from skimage.feature import local_binary_pattern, greycomatrix, greycoprops
from skimage.filters import gabor
import numpy as np
import pickle
import matplotlib.pyplot as plt
import harlick as har
import cv2
from PIL import Image
 
  
def extractFeature(imgOpencv):  
    # You may need to convert the color.
    #imgRGB = cv2.cvtColor(imgOpencv, cv2.COLOR_BGR2RGB)
    #im_pil = Image.fromarray(imgRGB)
    #img_gray = img.convert('L') #Converting to grayscale
    #img_arr = np.array(img_gray.getdata()).reshape(im_pil.size[1],im_pil.size[0]) #Converting to array

    img_graycv = cv2.cvtColor(imgOpencv, cv2.COLOR_BGR2GRAY)
    img_arr = img_graycv

    print("Starting Extraction")
    # LBP
    hist = desc.describe(img_arr) 
    feat_lbp = local_binary_pattern(img_arr,5,2,'uniform')
    lbp_hist,_ = np.histogram(feat_lbp,8)
    #print(lbp_hist)

    lbp_hist = np.array(lbp_hist,dtype=float)
    lbp_prob = np.divide(lbp_hist,np.sum(lbp_hist))
    lbp_energy = np.nansum(lbp_prob**2)
    lbp_entropy = -np.nansum(np.multiply(lbp_prob,np.log2(lbp_prob)))   
    # GLCM
    gCoMat = greycomatrix(img_arr, [2], [0],256,symmetric=True, normed=True)
    contrast = greycoprops(gCoMat, prop='contrast')
    dissimilarity = greycoprops(gCoMat, prop='dissimilarity')
    homogeneity = greycoprops(gCoMat, prop='homogeneity')    
    energy = greycoprops(gCoMat, prop='energy')
    correlation = greycoprops(gCoMat, prop='correlation')    
    feat_glcm = np.array([contrast[0][0],dissimilarity[0][0],homogeneity[0][0],energy[0][0],correlation[0][0]])
    # Gabor filter
    gaborFilt_real,gaborFilt_imag = gabor(img_arr,frequency=0.6)
    gaborFilt = (gaborFilt_real**2+gaborFilt_imag**2)//2
    gabor_hist,_ = np.histogram(gaborFilt,8)
    gabor_hist = np.array(gabor_hist,dtype=float)
    gabor_prob = np.divide(gabor_hist,np.sum(gabor_hist))
    gabor_energy = np.nansum(gabor_prob**2)
    gabor_entropy = -np.nansum(np.multiply(gabor_prob,np.log2(gabor_prob)))
    # Concatenating features(2+5+2)    
    concat_feat = np.concatenate(([lbp_energy,lbp_entropy],[hist],[feat_glcm],[gabor_energy,gabor_entropy]),axis=0)
    print(concat_feat)

def extractFeatureNew(imgOpencv):  
    # You may need to convert the color.
    #imgRGB = cv2.cvtColor(imgOpencv, cv2.COLOR_BGR2RGB)
    #im_pil = Image.fromarray(imgRGB)
    #img_gray = img.convert('L') #Converting to grayscale
    #img_arr = np.array(img_gray.getdata()).reshape(im_pil.size[1],im_pil.size[0]) #Converting to array

    img_graycv = cv2.cvtColor(imgOpencv, cv2.COLOR_BGR2GRAY)
    img_arr = img_graycv

    print("Starting Extraction")
    # LBP
    hist_lbp = desc.describe(img_arr)
    hist_harlick = har.extract_features(img_arr)
    print("harlick",str(hist_harlick))
    feat_lbp = local_binary_pattern(img_arr,5,2,'uniform')
    lbp_hist,_ = np.histogram(feat_lbp,8)

    lbp_hist = np.array(lbp_hist,dtype=float)

    lbp_prob = np.divide(lbp_hist,np.sum(lbp_hist))
    lbp_energy = np.nansum(lbp_prob**2)
    lbp_entropy = -np.nansum(np.multiply(lbp_prob,np.log2(lbp_prob)))   
    print(str(lbp_entropy),str(lbp_energy))
    # GLCM
    gCoMat = greycomatrix(img_arr, [2], [0],256,symmetric=True, normed=True)
    contrast = greycoprops(gCoMat, prop='contrast')
    dissimilarity = greycoprops(gCoMat, prop='dissimilarity')
    homogeneity = greycoprops(gCoMat, prop='homogeneity')    
    energy = greycoprops(gCoMat, prop='energy')
    correlation = greycoprops(gCoMat, prop='correlation')    
    feat_glcm = np.array([contrast[0][0],dissimilarity[0][0],homogeneity[0][0],energy[0][0],correlation[0][0]])
    # Gabor filter
    gaborFilt_real,gaborFilt_imag = gabor(img_arr,frequency=0.6)
    gaborFilt = (gaborFilt_real**2+gaborFilt_imag**2)//2
    gabor_hist,_ = np.histogram(gaborFilt,8)
    gabor_hist = np.array(gabor_hist,dtype=float)
    gabor_prob = np.divide(gabor_hist,np.sum(gabor_hist))
    gabor_energy = np.nansum(gabor_prob**2)
    gabor_entropy = -np.nansum(np.multiply(gabor_prob,np.log2(gabor_prob)))
    print(feat_glcm)
    print(hist_lbp)
    # Concatenating features(2+5+2)    
    concat_feat = np.concatenate((hist_lbp,hist_harlick,feat_glcm,[gabor_energy,gabor_entropy]),axis=0)
    print(concat_feat)
    gaborArr = []
    gaborArr.append(gabor_energy)
    gaborArr.append(gabor_entropy)
    return hist_lbp,hist_harlick,feat_glcm,gaborArr

#img  =	cv2.imread('C:/Users/Kasun/source/repos/PythonApplication3/FinalImages1/test1.png')
img  =	cv2.imread('/home/lahiru/Pictures/Benign.jpg')

extractFeatureNew(img)
