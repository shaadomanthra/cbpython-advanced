from tkinter import *
from cv2 import cv2
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageTk
import threading

class BarView:

    def main(self):
        print("This is from main, BarView")
        window = Tk()
        window.title("Barcode & Qrcode Detector")
        frame = Frame(window,padx=20,pady=20,bg="#FF5733")
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.label = Label(frame)
        self.label.grid(row=0,column=0)

        b1 = Button(frame, text="Start",command=self.webcam)
        b1.grid(row=1,column=0)

        b2 = Button(frame, text="Stop",command=self.stop)
        b2.grid(row=1, column=1)

        window.mainloop()

    def webcam(self):
        self.stop = False
        self.cap = cv2.VideoCapture(0)

        t = threading.Thread(target=self.start,args=())
        t.start()


    def start(self):

        try:
            # capture the image
            ret, image = self.cap.read()

            #  resize the image frame to half
            image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            # change the image to gray scale for faster processing
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            barcodes = pyzbar.decode(gray)
            print(barcodes)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                text = barcode.data.decode('utf-8')
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (51, 51, 255), 2)

            # Convert the opencv image to tkinter format
            image_array = Image.fromarray(image)
            image_tk = ImageTk.PhotoImage(image_array)

            self.label.config(image=image_tk)
            self.label.image = image_tk

            if self.stop == False:
                self.label.after(10,self.start)
            else:
                self.label.image = None

        except:
            print("Some error happened in start function")



    def stop(self):
        print("stop")
        self.stop = True



