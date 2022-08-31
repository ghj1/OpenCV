import sys
import cv2
import numpy as np


cap1 = cv2.VideoCapture('videos/woman.mp4')
cap2 = cv2.VideoCapture('videos/raining.mp4')
fps = round(cap1.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (50,150,0), (80,255,255))
    cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    if cv2.waitKey(delay) == 27: break 

cap1.release()
cap2.release()
cv2.destroyAllWindows()

# while True:
#     ret, frame = cap1.read()
#     cv2.imshow('cap1', frame)
#     if cv2.waitKey(delay) == 27: break
# cap1.release()
# cv2.destroyAllWindows()

