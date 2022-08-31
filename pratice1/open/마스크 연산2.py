import cv2 
import numpy as np 


src = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = np.zeros_like(src)
dst = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)
# h, w = image.shape[:2]
# mask = np.zeros((h ,w), cv2.unit8)

cv2.circle(mask, (380, 210), 100, (255,255,255), -1)
masked = cv2.bitwise_and(src, mask)

cv2.copyTo(src, mask, dst)
cv2.imshow('img',masked)
cv2.waitKey()
cv2.destroyAllWindows()



