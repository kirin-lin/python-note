import cv2

img = cv2.imread('sample.png', 2)

if cv2.imwrite("grayscale.png", img):
    msg = "Write Success"
else:
    msg = "Write Failure"

cv2.imshow(msg, img)

cv2.waitKey()
cv2.destroyAllWindows()
