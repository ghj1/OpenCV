import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread('images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('images/square.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.bitwise_and(src1,src2)
dst2 = cv2.bitwise_or(src1,src2)
dst3 = cv2.bitwise_xor(src1,src2)
dst4 = cv2.bitwise_not(src1)

# titles = ['dst1', 'dst2', 'dst3', 'dst4']
# for t in titles:
#     cv2.imshow(t,eval(t))
plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'),plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'),plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'),plt.title('bitwise_and')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'),plt.title('bitwise_or')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'),plt.title('bitwise_xo')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'),plt.title('bitwise_not')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
