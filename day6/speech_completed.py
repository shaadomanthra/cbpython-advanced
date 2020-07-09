import speech_recognition as sr         # import speech library
import webbrowser
r = sr.Recognizer()                     # create a speech object
file = sr.AudioFile('sample.wav')       # take file path
with file as source:                    # load the file
    audio = r.record(source)            # record from source
text = r.recognize_google(audio)        # recognize the speecch

if text == 'open Facebook':
    print("Opening the brwoser and facebook website")
    webbrowser.open("https://facebook.com")
else:
    print("The speech is not clear")

