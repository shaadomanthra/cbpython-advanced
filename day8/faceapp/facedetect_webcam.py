from cv2 import cv2
import numpy as np

# Load the cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the webcamera
cap = cv2.VideoCapture(0)

# Capture frame (image) continuously using infinite loop
while True:
    # read func will capture a frame
    ret, frame = cap.read()
    # turn the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #  use detectmultiscale func to detect the face which returns face coordinates
    face_rects = face_cascade.detectMultiScale(gray, 1.7, 11)
    # draw the recctangle on the frame
    for (x,y,w,h) in face_rects:
        y = int(y - 0.15*h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        break
    # show the window with image(frame)
    cv2.imshow('Face Detector', frame)

    # wait for escape key
    c = cv2.waitKey(1)
    if c == 27:
        break

#  release the memory buffer for the camera
cap.release()
cv2.destroyAllWindows()
