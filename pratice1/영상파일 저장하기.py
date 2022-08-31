import sys
import cv2


img1 = cv2.imread('images/cat.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imwrite('images/cat_gray.jpg',img1)
# image = [cv2.IMWRITE_JPEG_QUALITY, 90])

if img2 is None:
    print('Image save failed!')
    sys.exit()
cv2.namedWindow('image')
cv2.imshow("image", img2)
cv2.waitKey()

cv2.destroyAllWindows()