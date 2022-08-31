import cv2

src = cv2.imread('images/airplane.bmp')

dst1 = cv2.flip(src,1) # 좌우대칭
dst2 = cv2.flip(src, 0) #상하 대칭
dst3 = cv2.flip(src, -1) # 좌우상하 대칭


cv2.imshow('dst1', dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()