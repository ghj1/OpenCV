import cv2
import numpy as np 
img = np.ones((,256), dtype=np.uint8) * 255
cv2.circle(img, (128,128), 500, (0,0,0), -1)
cv2.imshow('f', img)
cv2.waitKey()
cv2.destroyAllWindows()
# src1 =cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# dst1 = cv2.subtract(src1,  )