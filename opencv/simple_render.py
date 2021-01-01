import cv2

img = cv2.imread("sample.png")

cv2.imshow("Sample", img)

cv2.waitKey()
cv2.destroyAllWindows()
