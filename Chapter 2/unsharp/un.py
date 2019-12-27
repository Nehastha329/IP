import cv2
image = cv2.imread("8.jpg")
gaussian_3 = cv2.GaussianBlur(image, (9,9), 10.0)
unsharp_image = cv2.addWeighted(image, 3.5, gaussian_3, -0.5, 0)
cv2.imwrite("8_unsharp.jpg", unsharp_image)
cv2.imshow('',unsharp_image)
cv2.imshow('original',image)
cv2.waitKey(1000000)