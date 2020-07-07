from PIL import Image               # import the image package

im = Image.open('sample.jpg')       # load image
print(im.format, im.size)           # print the format size
im = im.convert("L").rotate(90)     # turn to grayscale and rotate
im.show()                           # open in windows
im.save('updated.jpg', quality=50)  # save it to computer
