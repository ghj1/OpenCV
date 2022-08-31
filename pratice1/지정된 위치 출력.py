import cv2
import numpy as np 
import sys

img = cv2.imread('images\cat.bmp')
(x , y, z) = img.shape
cv2.imshow('image',img)
cv2.resizeWindow('image',y+100,x+100)
cv2.moveWindow('image',300,300)
cv2.waitKey()
cv2.destroyAllWindows()

# image = cv2.imread('images\cat.bmp')
# title1= 'NORMAL'
# cv2.namedWindow(title1,cv2.WINDOW_NORMAL)
# if image is None:
#     print('Image load failed!')
#     sys.exit()
# cv2.imshow(title1, image)
# cv2.resizeWindow(title1, 580, 740)
# cv2.moveWindow(title1,300,300)
# cv2.waitKey()

# cv2.destroyAllWindows()

