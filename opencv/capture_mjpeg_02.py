import cv2
import numpy as np
import urllib.request

stream=urllib.request.urlopen('https://cctvc.freeway.gov.tw/abs2mjpg/bmjpg?camera=236')
bytes=bytes()

while True:
    bytes+=stream.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]

        img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('Window name', img)
        if cv2.waitKey(1) != -1:
            exit(0)
