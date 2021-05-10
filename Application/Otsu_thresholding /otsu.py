import numpy as np
import cv2
import matplotlib.pyplot as plt

# load & convert to gray 
image = cv2.imread("HeLa.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("binary", image_gray)
#cv2.waitKey(0)

histg = cv2.calcHist([image_gray], [0], None, [256], (0,256))

within = []
for i in range(len(histg)) :# 256
    x,y = np.split(histg,[i]) 
    x1 = np.sum(x) / (image.shape[0] * image.shape[1]) # weight of class1 
    y1 = np.sum(y) / (image.shape[0] * image.shape[1])
    x2 = np.sum([j*t for j,t in enumerate(x)]) / np.sum(x) # mean of class1 
    y2 = np.sum([j*t for j,t in enumerate(y)]) / np.sum(y)
    x3 = np.sum([(j-x2)**2 *t for j,t in enumerate (x)] / np.sum(x)) # variance of class1 
    x3 = np.nan_to_num(x3) # change "nan" to zero 
    y3 = np.sum([(j-y2)**2 *t for j,t in enumerate (y)] / np.sum(y)) 
    within.append(x1*x3 +y1*y3)

min_ = min(within)
threshold = within.index(min_)
ret, th = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)

# Checking code with library 
ret2,th2 = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Concatenate three images 
numpy_horizontal_concat = np.concatenate(( image_gray, th, th2), axis=1)

cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
cv2.waitKey(0)
