import cv2

camera = cv2.VideoCapture("https://cctvc.freeway.gov.tw/abs2mjpg/bmjpg?camera=236")

if cv2.VideoCapture.isOpened(camera):
    print("Open Success.")
else:
    print("Open Failure.")

while camera.isOpened():
    ret, frame = camera.read()
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(25)
    if key != -1:
        break

cv2.destroyAllWindows()
