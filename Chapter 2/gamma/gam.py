import numpy as np
import cv2
im = cv2.imread('a.jpg')
im = im/255.0
transformation = cv2.pow(im,3)
cv2.imshow('Original Image',im)
cv2.imshow('Transformation',transformation)
cv2.imwrite('3.jpg',im)

transformation1=cv2.pow(im,0.2)
cv2.imshow('Transformation1',transformation1)
cv2.imwrite('4.jpg',im)
cv2.waitKey(0)