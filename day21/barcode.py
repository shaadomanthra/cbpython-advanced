from cv2 import cv2
from PIL import Image
from pyzbar import pyzbar

# First step is to capture the video
cap = cv2.VideoCapture(0)
while True:
    # To capture the photo
    ret, image = cap.read()
    image = cv2.resize(image,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    print(barcodes)

    cv2.imshow('Barcode Detector',gray)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

