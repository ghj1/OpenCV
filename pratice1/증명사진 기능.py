import cv2
import sys

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    file = 'photo.jpg'
   
    cv2.rectangle(frame, (180,90),(500,400),(255,255,255),3)
    cv2.putText(frame, 'press enter key!',(600,500), cv2.FONT_HERSHEY_COMPLEX,0.8, (255,0,0))
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(10)
    if key == 27: break
    elif key == 13 : 
        img_frame = frame.copy()
        img_size = img_frame[90:400, 100:500]
        cv2.imwrite(file, img_size)
        print(file, '저장됨')

cap.release()
cv2.destroyAllWindows()


# import datetime
# file ='photo'+datetime.datetime.now().strftime('%Y-%m-%d %H %M')+'.jpg'


