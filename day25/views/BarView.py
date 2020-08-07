from tkinter import *
from tkinter import messagebox
from cv2 import cv2
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageTk #for converting opencv image to tkinter image
import threading #to run processess simultaneously
from models.BarModel import BarModel


class BarView:

    def main(self):
        print("This is main from Barview")

        window = Tk()
        window.title("Barcode & Qrcode detector")

        frame = Frame(window,padx=10,pady=10,bg="#ff5733")
        frame.grid(row=0,column=0)
        self.label = Label(frame)
        self.label.grid(row=0,column=0,columns=4)

        b1 = Button(frame, text="start",command=self.webcam)
        b1.grid(row=1,column=0,padx=10,pady=10,sticky='nesw')

        b2 = Button(frame, text="stop", command = self.stop)
        b2.grid(row=1,column=1,padx=10,pady=10,sticky='nesw')

        b3 = Button(frame, text="Capture",command = self.capture,padx=10,pady=10)
        b3.grid(row=1,column=2,padx=10,pady=10,sticky='nesw')

        b4 = Button(frame, text="History", command=self.history, padx=10, pady=10)
        b4.grid(row=1, column=3, padx=10, pady=10, sticky='nesw')

        self.label2 = Label(frame, text="show history")
        self.label2.grid(row=2,column=0,padx=20,pady=20,columns=4)

        window.mainloop()

    def webcam(self):
        print("Webcam function")
        self.stop = False
        self.cap = cv2.VideoCapture(0)

        # To start the webcam as a seperate process we will use threading
        # this will enable us to run two or threee processes simultaneosly
        t = threading.Thread(target=self.start, args=())
        t.start()

    def start(self):
        print("start function")
        try:
            ret, image = self.cap.read()
            image = cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
            print("completed image capture")
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            color = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            print("changed the color")
            barcodes = pyzbar.decode(gray)
            print(barcodes)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(color, (x, y), (x + w, y + h), (0, 0, 255), 2)
                text = barcode.data.decode('utf-8')
                username  = 'krishna teja'

                # create a model object
                bm = BarModel()

                if bm.fetch(text,username)==None:
                    bm.insertBarcode(text,username)

                cv2.putText(color, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (51, 51, 255), 2)

            # Convert the opencv image to tkinter image
            self.image_array =Image.fromarray(color)
            image_tk = ImageTk.PhotoImage(self.image_array)

            # update the image in the tkinter window
            self.label.config(image=image_tk)
            self.label.image = image_tk

            # refresh the label with recursive call
            if self.stop == False:
                self.label.after(10,self.start)
            else:
                self.label.image = None
        except:
            print("Some error")

    def stop(self):
        print("stop function")
        self.stop = True

    def capture(self):
        print("Capture function")
        self.image_array.save('images/1.jpg')
        messagebox.showinfo("Image Capture","Image frame is captured")

    def history(self):
        bm = BarModel()
        result = bm.fetchall("krishna teja")
        print(result)
        self.label2.config(text=result)