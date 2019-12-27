import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('h.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf1 = cdf * hist.max()/ cdf.max()

plt.plot(cdf1, color = 'r')
plt.hist(img.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper right')
plt.show()
plt.saveimg('g.jpg')

