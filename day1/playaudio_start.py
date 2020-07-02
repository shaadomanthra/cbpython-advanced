# # Creating an audio file and play
# import google text to speech library
from gtts import gTTS

# import os package
import os
# process text to audio
tts = gTTS("Hello Krishna Teja")
# save the file
tts.save("hello.mp3")

# play the file
os.system("mpg321 hello.mp3") # command for mac
# os.system("start hello.mp3")