import cv2
import numpy as np 

src = cv2.VideoCapture('videos/road.mp4')
fps = round(src.get(cv2.CAP_PROP_FPS))
delay = round(1000/fps)

while True:
    ret, frame = src.read()
    cv2.imshow('src', frame)

    if cv2.waitKey(10) ==27:
        break 


edges = cv2.Canny(frame, 50,150)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160, minLineLength=100, maxLineGap= 5)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None: 
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv2.line(dst, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

while True:
    ret, frame = src.read()

    cv2.imshow('src', frame)
    cv2.imshow('dst', dst)

    if cv2.waitKey(10) ==27:
        break 

# cv2.imshow('src', frame)
# cv2.imshow('dst', dst)
src.release()
cv2.destroyAllWindows()