import cv2
import os
import glob

img_files = glob.glob('images\*')

cv2.namedWindow('Image Slide Show', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Image Slide Show', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)    

cnt = len(img_files)
idx = 0
ESC = 27
while True:
    img = cv2.imread(img_files[idx % cnt])
    if img is None:
        print("Image load failed!")
        break
    cv2.imshow('image',img)
    if cv2.waitKey(1000) == ESC:
        break
    idx += 1
cv2.destroyAllWindows()



