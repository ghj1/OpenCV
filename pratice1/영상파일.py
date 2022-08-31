import sys
import cv2

print('Hello OpenCV', cv2.__version__)

# image = cv2.imread('images\cat.bmp') # 파이썬 소스가 있는 디렉토리 아래에 images 디렉토리에 cat.bmp 파일 읽어오기
image = cv2.imread('images\cat.bmp',cv2.IMREAD_UNCHANGED) # 영상 파일 속성 그대로 읽기
# image = cv2.imread('images\cat.bmp',cv2.IMREAD_COLOR) # BGR 컬러 영상으로 읽기(기본값)
# image = cv2.imread('images\cat.bmp',cv2.IMREAD_GRAYSCALE) # 그레일 컬러 영상으로 읽기

print(image.shape)
print(image)
if image is None:
    print('Image load failed!')
    sys.exit()
cv2.namedWindow('image')
cv2.imshow("image", image)
cv2.waitKey()

cv2.destroyAllWindows()

# 터미널에서 지금 실행하는 소스가 있는(영상파일.py) 위치에 가서 실행해야 한다.  
# PS C:\Users\PC021> cd c:/python/rapa/opencv
