# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:07:20 2019

@author: SRIJAN
"""


import cv2 
import numpy as np
from matplotlib import pyplot as plt

"""mathematical way"""
# =============================================================================
# img = cv2.imread('pic.jpg')
# 
# hist,bins = np.histogram(img.flatten(),256,[0,256])
# 
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
# 
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(), 256, [0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'best')
# plt.show()
# 
# cdf_m = np.ma.masked_equal(cdf,0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# cdf = np.ma.filled(cdf_m,0).astype('uint8')
# 
# img2 = cdf[img]
# 
# cv2.imshow('image',img2)
# 
# =============================================================================

"""OpenCV way"""

img = cv2.imread('download.jpg', 1)
 
#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
#-----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl,a,b))
#-----Converting image from LAB Color model to RGB model--------------------
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imwrite('final.jpg', final)


