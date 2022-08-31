import cv2
import numpy as np 

vi1 = cv2.VideoCapture('videos/video1.mp4')
vi2 = cv2.VideoCapture('videos/video2.mp4')

frame_c1 = round(vi1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_c2 = round(vi2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vi1.get(cv2.CAP_PROP_FPS)
effect_frame = int(fps*2)
delay = round(100/fps)
w = round(vi1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(vi2.get(cv2.CAP_PROP_FRAME_HEIGHT))

for i in range(frame_c1 - effect_frame):
    ret1, frame1 = vi1.read()
    if not ret1: break

    cv2.imshow('vi',frame1)
    if cv2.waitKey(delay) == 27: break 

for i in range(effect_frame): # 항상 정수값이 들어가야 한다. 
    ret1, frame1 = vi1.read()
    ret2, frame2 = vi2.read()
    if not (ret2 or ret1): break 

    dx = int(w*i/effect_frame)

    frame = np.zeros((h,w,3),dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:,0:dx, :]
    frame[:,dx:w, :] = frame1[:,dx:w, :]
    cv2.imshow('vi',frame)
    if cv2.waitKey(delay) == 27: break 

for i in range(effect_frame, frame_c2):
    ret2, frame2 = vi2.read()
    if not ret2: break 
    
    cv2.imshow('vi', frame2)
    if cv2.waitKey(delay) == 27: break 
vi1.release()
vi2.release()
cv2.destroyAllWindows()




