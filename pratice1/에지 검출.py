import cv2
import numpy as np 

# src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE) 
src = cv2.imread('images/building.jpg', cv2.IMREAD_GRAYSCALE)
# dx = cv2.Sobel(src, -1,1,0, delta= 128)
# dy = cv2.Sobel(src, -1,0,1, delta= 128)

# cv2.imshow('src', src)
# cv2.imshow('dx',dx)
# cv2.imshow('dy', dy)
# cv2.waitKey()

cv2.destroyAllWindows()

# 캐니 에지 검출 
dst  = cv2.Canny(src, 50,150) 
dst1  = cv2.Canny(src, 25,75) 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst1', dst1)
cv2.waitKey()

cv2.destroyAllWindows()
