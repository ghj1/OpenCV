import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('images/cat.bmp')
imgBGR2 = cv2.imread('images/penguin.jpg')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('images/cat.bmp',cv2.IMREAD_GRAYSCALE)
imgGray2 = cv2.imread('images/penguin.jpg',cv2.IMREAD_GRAYSCALE)


plt.subplot(221), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(222), plt.axis('off'), plt.imshow(imgGray, cmap = 'gray')
plt.subplot(223), plt.axis('off'), plt.imshow(imgRGB2)
plt.subplot(224), plt.axis('off'), plt.imshow(imgGray2, cmap = 'gray')
plt.show()



# plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
# plt.subplot(행, 열, 순차적인 번호)

# pratice
# 하나의 윈도우에 여러 이미지를 출력하는게 가능하다는 것이 장점이다. 