import cv2 

src = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('images/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

# if src is None or mask is None or dst is None:
#     print()


dst[mask > 0] = src[mask > 0 ]
cv2.copyTo(src, mask, dst) # dst에 바로 저장 

# smd = cv2.copyTo(src, mask, dst)
# cv2.imshow('img', smd)
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()

