import cv2
import numpy as np 
import sys

img = cv2.imread('images/scanned.jpg')

src = cv2.pyrDown(img)

h,w = src.shape[:2]
dw = 500 
dh = round(dw*297/210)

srcQuad = np.array([[30,30],[30,h-30],[w-30,h-30],[w-30, 30]], np.float32)
dstQuad = np.array([[0,0],[0,dh-1],[dw-1,dh-1],[dw-1,0]], np.float32)
dragSrc = [False, False, False,False]

def drawROI(img, corners):
    cpy = img.copy()

    c1 = (192, 192, 255) # 코너 원 색상
    c2 = (128, 128, 255) # 라인 색상
    corners = corners.astype(int)
    for pt in corners:
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)

    cv2.line(cpy, tuple(corners[0]), tuple(corners[1]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1]), tuple(corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2]), tuple(corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3]), tuple(corners[0]), c2, 2, cv2.LINE_AA)

    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)

    return disp 

disp = drawROI(src, srcQuad)

cv2.imshow('img', disp)


def onMouse(event, x, y, flags, param):
    global srcQuad , dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i]-(x,y)) < 25:
                ptOld = (x,y)
                break 

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            dx = x - ptOld[0]
            dy = y - ptOld[1]
            srcQuad[i] += (dx, dy)

            cpy = drawROI(src, srcQuad)
            cv2.imshow('img', cpy)
            ptOld =(x,y)
            break 

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key =cv2.waitKey()
    if key == 13:
        break 
    elif key == 27:
        cv2.destroyAllWindows('img')
        sys.exit()
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags = cv2.INTER_CUBIC)    


cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()