import cv2
import sys

img = cv2.imread('images/cat.jpg')
cv2.imshow('image', img)

while True:
    key = cv2.waitKey()
    if key == 27: # cv2.waitkey() 는 s키를 두번 쳐야 된다. 
        break 
    elif key == ord('s') or key == ord('S'):
        img = ~img  # ~: not이라는 의미 
        cv2.imshow('image', img)
cv2.destroyAllWindows()