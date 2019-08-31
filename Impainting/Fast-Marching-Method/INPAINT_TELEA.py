# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:19:03 2019

@author: SRIJAN
"""

import numpy as np
import cv2

img = cv2.imread('./images/1.jpg')
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow('image', resized_img)


resized_img = cv2.line(resized_img,(0,100),(831,100),(255,255,255),5)
resized_img = cv2.line(resized_img,(0,340),(831,340),(255,255,255),5)
#cv2.imshow('image', resized_img)

back = np.zeros((832,624,1), np.uint8)
mask = cv2.line(back,(0,100),(831,100),(255,255,255),5)
mask = cv2.line(back,(0,340),(831,340),(255,255,255),5)

#cv2.imshow('mask',mask)

dst = cv2.inpaint(resized_img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)