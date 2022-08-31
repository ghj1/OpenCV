import cv2
import numpy as np 

print('Hello OpenCV', cv2.__version__)

image = np.zeros((300,400), np.uint8)
# print(image)
# print(image.shape)
image.fill(200)

cv2.imshow('Window title', image)
cv2.waitKey(0) # 0으로 안채워도 상관없다. 

cv2.destroyAllWindows()


# 300행, 400열 크기의 행렬 생성하여 행렬의 모든 원소의 값을 회색(200)으로 지정한 것
# 이 행렬을 'window title'이름의 윈도우에 영상으로 표시