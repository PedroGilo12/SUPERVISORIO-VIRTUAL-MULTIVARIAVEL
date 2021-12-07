from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

img_uno = ImageTk.PhotoImage(Image.open("imagens/arduino_uno_small.png"))
img_nano = ImageTk.PhotoImage(Image.open("imagens/arduino_nano_small.png"))

class Application():
    def __init__(self):
        self.root = root
        self.tela1()
        self.frames_da_tela1()
        self.widgetsframe1()
        self.widgetsframe2()
        root.mainloop()

    def tela1(self):
        self.root.title("SVM - Supervisório Virtual Multivariável")
        self.root.geometry("700x600")
        self.root.configure(background = "#ACCBFF")
        self.root.resizable(False, False)

    def frames_da_tela1(self):
        self.frame1 = Frame(self.root, background = "#E1E1E1")
        self.frame1.place(relx=0.02, rely= 0.29, relwidth=0.96, relheight=0.69)

        self.frame2 = Frame(self.root, background = "white")
        self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.25)

    def widgetsframe1(self):
        #botão Iniciar
        self.bt_init = Button(self.frame1, text = "Iniciar", background="white")    
        self.bt_init.place(relx=0.67,rely=0.95,relwidth=0.16,relheight=0.05)  
        #botão Fechar
        self.bt_close = Button(self.frame1, text = "Fechar", background="white")
        self.bt_close.place(relx=0.84,rely=0.95,relwidth=0.16,relheight=0.05)

        #self.imagem = Label(self.frame1, text = "IMAGEM", image = img_uno, background = "#E1E1E1")
        #self.imagem.place(relx=0.25,rely=0.01,relwidth=0.50,relheight=0.75)


    def widgetsframe2(self):
        self.menu_text = Label(self.frame2, text = "SELECIONE O HARDWARE ALVO", background = "white")
        self.menu_text.pack()

        self.marker_uno = Checkbutton(self.frame2, text = "Arduino uno", command = self.ArduinoUnoMarker)
        self.marker_uno.place(relx = 0.25, rely=0.2, relwidth=0.25, relheight=0.25)

        self.marker_nano = Checkbutton(self.frame2, text = "Arduino nano", command = self.ArduinoNanoMarker)
        self.marker_nano.place(relx = 0.50, rely=0.2, relwidth=0.25, relheight=0.25)

    def ArduinoUnoMarker(self):
        self.imagem = Label(self.frame1, text = "IMAGEM", image = img_uno, background = "#E1E1E1")
        self.imagem.place(relx=0.25,rely=0.01,relwidth=0.50,relheight=0.75)

    def ArduinoNanoMarker(self):
        self.imagem = Label(self.frame1, text = "IMAGEM", image = img_nano, background = "#E1E1E1")
        self.imagem.place(relx=0.25,rely=0.01,relwidth=0.50,relheight=0.75)





Application()
