import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('images/cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # 이줄을 주석처리 하고 

plt.axis('off')
plt.imshow(imgRGB) # 여기에 imgBGR을 입력해 출력해보기 
plt.show()

imgGray = cv2.imread('images/cat.bmp',cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap = 'gray')
plt.show()
# plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
# plt.subplot(행, 열, 순차적인 번호)
