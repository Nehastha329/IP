import cv2
image = cv2.imread("s.jpg")
new = cv2.GaussianBlur(image, (9,9), 0)
unsharp_image = cv2.addWeighted(image, 3, new, -1, 0)
cv2.imshow('output',unsharp_image)
cv2.imshow('Orginal',image)
cv2.imwrite('aaa.jpg',unsharp_image)
cv2.waitKey(1000000000)