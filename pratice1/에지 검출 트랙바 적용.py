import cv2
import numpy as np 
import sys

def onTrackbar(th):
    rep_edge = cv2.Canny(rep_gray, th, th*2,5)
    h, w = src.shape[:2]
    cv2.rectangle(rep_edge, (0,0,w,h),255, -1)
    color_edge = cv2.bitwise_and(rep_img, rep_img, mask=rep_edge)
    cv2.imshow('color edge', color_edge)

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_COLOR)

th = 50 
rep_img = cv2.repeat(src, 1,2)
rep_gray = cv2.cvtColor(rep_img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('color edge', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Cannt th', 'color edge', th, 100, onTrackbar)
onTrackbar(th)

cv2.waitKey()
cv2.destroyAllWindows()