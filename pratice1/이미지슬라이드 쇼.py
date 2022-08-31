import os 
import glob
import cv2
import sys 


# file_list = os.listdir('images')
# img_files = [file for file in file_list if file.endswith('.jpg')] # 확장자가 jpg인것만 불러오기
img_files = glob.glob('images\*.jpg')

title = 'NORMAL'
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# 위아래 'image'가 똑같아야 한다. 


for i in range(len(img_files)):
    image = cv2.imread(img_files[i])
    if image is None:
        print('Image load failed!')
        
    
    cv2.imshow("image",image)
    cv2.waitKey()
cv2.destroyAllWindows()

 
# cnt = len(img_files)
# idx = 0 
# while True:
#     img = cv2.imread(img_files[idx])

#     if img is None:
#         print('Image load failed!')
#         break
#     cv2.imshow('title', img)
#     if cv2.waitKey(1000) >= 0:
#         break
#     idx += 1 
#     if idx >= cnt:
#         idx = 0 
  



