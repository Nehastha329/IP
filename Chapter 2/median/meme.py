import cv2
import numpy as np
image = cv2.imread('md.jpg')
md = cv2.medianBlur(image, 5)
med = np.concatenate((image, md), axis=1) 
cv2.imshow('output', med)
cv2.waitKey(0)
