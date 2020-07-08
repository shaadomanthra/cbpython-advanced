# import the image package
from PIL import Image
# load image
im = Image.open('sample.jpg')
print(im.format)
print(im.size)
# turn to grayscale
im = im.convert("L")

# rotate image
im = im.rotate(180)
# open in window
im.show()

# save it to computer
im.save("new.jpg")

# write a python prograam to convert a HD image(>1000px) to
# low resolution of 100px


