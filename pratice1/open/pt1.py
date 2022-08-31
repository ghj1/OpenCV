import numpy as np
import cv2

b_window = np.zeros((200,300),np.uint8)
b_window.fill(100)

img = cv2.imread('images\cat.bmp',cv2.IMREAD_COLOR)
(x , y, z) = img.shape
title = 'image'
cv2.namedWindow(title,cv2.WINDOW_AUTOSIZE)
cv2.imshow(title,img)
cv2.resizeWindow(title,y+100,x+100)
cv2.moveWindow(title,300,300)
cv2.waitKey()
cv2.destroyAllWindows()

print(img.shape)