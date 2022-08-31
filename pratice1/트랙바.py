import cv2
import numpy as np 

def on_R(pos):
    img [:, :, 0] = pos
    cv2.imshow('img', img)
def on_G(pos):
    img [:, :, 1] = pos
    cv2.imshow('img', img)
def on_B(pos):
    img [:, :, 2] = pos
    cv2.imshow('img', img)

img = np.full((480,640,3),(255,255,255), dtype= np.uint8) 

cv2.namedWindow('img')
cv2.createTrackbar('R', 'img', 0, 255, on_R)
cv2.createTrackbar('G', 'img', 0, 255, on_G)
cv2.createTrackbar('B', 'img', 0, 255, on_B)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
