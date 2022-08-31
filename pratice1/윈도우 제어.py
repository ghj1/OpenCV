import numpy as np 
import cv2 

image = np.zeros((200,300), np.uint8)
image.fill(255)

title1, title2 = 'NORMAL','AUTOSIZE'
cv2.namedWindow(title1,cv2.WINDOW_NORMAL)
cv2.namedWindow(title2,cv2.WINDOW_AUTOSIZE)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)

cv2.waitKey()
cv2.destroyAllWindows() # 함수는 열려있는 모든 창을 닫음

# cv2.destroyWindow() 함수는 지정한 창 하나만 닫고 
# cv2.moveWindow(winname, x,y) -> None 창 위치 이동 winname: 창이름 x,y 이동할 위치 좌표
# cv2.resizeWindow(winname, width, height) -> None 1: 창 이름, 2: 변경할 창의 가로크기 3: 변경할 창의 세로 크기
# 창 생성 시 cv2.WINDOW_NORMAL 속성으로 생성되어야 동작
# 영상 출력 부분의 크기만을 고려함 (제목 표시줄, 창 경계는 고려되지 않음)