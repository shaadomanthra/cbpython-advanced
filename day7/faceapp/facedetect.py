## detect face and draw rectangles

# import packages (pip install opencv-python)
from cv2 import cv2
import sys

# path for image and cascade
imagePath = 'images/f1.jpg'
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image & convert to gray scale
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
print(faces)

# # Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
# #
# # # # open the image widow to display
cv2.imshow("Faces found", image)
cv2.waitKey(0)

# Saving the image
# cv2.imwrite(saveimagePath, image)
