import cv2
image=cv2.imread('m.png',0)
cv2.imshow('greyscale',image)
new=cv2.blur(image(0.2,0.2))
cv2.imshow('output',new)
cv2.imwrite('9.png',new)
cv2.waitKey(100000000)

