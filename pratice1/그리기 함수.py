import cv2
import numpy as np 

img = np.full((400,400,3),255, np.uint8)

cv2.line(img, (50,50), (200,50),(0,0,255), 5)
cv2.line(img, (50,60), (150,160),(255,0,0))


cv2.imshow('line', img)
cv2.waitKey()
cv2.destroyAllWindows()