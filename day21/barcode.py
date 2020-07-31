from cv2 import cv2
from pyzbar import pyzbar

# Invoke webcamera
cap = cv2.VideoCapture(0)
while True:
    # To capture the photo
    ret, image = cap.read()
    image = cv2.resize(image,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    print(barcodes)

    for barcode in barcodes:
        (x,y,w,h) =barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

        # d = barcode.data.decode('utf-8')
        # print(d)

    cv2.imshow('Barcode Detector',image)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

