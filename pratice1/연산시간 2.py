import time
import numpy as np 
import cv2


cap = cv2.VideoCapture('videos/totoro.mp4')
# fps = round(cap.get(cv2.CAP_PROP_FPS))
# delay = round(1000 / fps)
tm = cv2.TickMeter()
tm.reset()
tm.start()
t1 = time.time()

while True:
    ret, frame = cap.read()

    if not ret: break

    cv2.imshow('vo', frame)

    if cv2.waitKey() == 27:
        break


tm.stop()
cv2.destroyAllWindows()
print('time: ', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))