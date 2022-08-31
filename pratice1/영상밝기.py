import cv2
import numpy as np 

src = cv2.imread('images/lenna.bmp')
# dst = cv2.add(src, 100) 
#dst2 = src + 100
#dst2 = np.clip(src + 100., 0, 255).astype(np.uint8) 
# 100. 소수점을 입력해야 결과값이 잘 나온다. 

# cv2.imshow('sr', src)
# cv2.imshow('ds', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

dst1 = cv2.add(src, 100)