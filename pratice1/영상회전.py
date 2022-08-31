import math 
import cv2
import sys
import numpy as np 


src = cv2.imread('images/parasol.jpg') 

if src is None:
    print("Image load failed")
    sys.exit()

# 영상의 회전 
# rad = 20*math.pi /180     
# aff = np.array([[math.cos(rad),math.sin(rad), 0],
#                 [-math.sin(rad), math.cos(rad), 0]],
#                                  dtype = np.float32)
#dst = cv2.warpAffine(src, aff, (0,0))

# 영상의 중앙 기준 회전 
cp = (src.shape[1]/2 , src.shape[0]/2)
rot = cv2.getRotationMatrix2D(cp, 20,1)

dst = cv2.warpAffine(src, rot, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()