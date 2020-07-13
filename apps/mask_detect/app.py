from cv2 import cv2
import numpy as np

# Load the cascade file
cascade = cv2.CascadeClassifier('nose.xml')

# Load the webcamera
cap = cv2.VideoCapture(0)

# Capture frame (image) continuously using infinite loop
while True:
    # read func will capture a frame
    ret, frame = cap.read()
    # turn the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #  use detectmultiscale func to detect the nose which returns nose coordinates
    rects = cascade.detectMultiScale(gray, 1.7, 11)
    # draw the recctangle on the frame

    print(rects)

    for (x,y,w,h) in rects:
        y = int(y - 0.15*h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        cv2.putText(frame, "No Mask", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        break
    else:
        cv2.putText(frame, "Detected Mask", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    # show the window with image(frame)
    cv2.imshow('Mask Detector', frame)

    # wait for escape key
    c = cv2.waitKey(1)
    if c == 27:
        break

#  release the memory buffer for the camera
cap.release()
cv2.destroyAllWindows()
