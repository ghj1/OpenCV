import cv2
import numpy as np 
import random

#img = np.full((480,640,3),(255,255,255), dtype= np.uint8) 

oldx =  oldy = -1 

# def random_color():
#     return tuple(sorted([i for i in range(256)]*3, key=lambda x:random.random())[:3])

def random_size():
    return random.randint(10,100)

def on_mouse(event, x, y, flags):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx,oldy),(x,y),(0,0,255), 3, cv2.LINE_AA)
            cv2.imshow('img', img)
            oldx, oldy = x,y
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (oldx, oldy),random_size(), random.randint(), -1, cv2.LINE_4)
        cv2.imshow('img', img)
        oldx, oldy = x,y

img = np.full((480,640,3),(255,255,255), dtype= np.uint8) 
# img = np.ones((480,640,3), dtype=np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse, img)
cv2.waitKey()

# 다시  