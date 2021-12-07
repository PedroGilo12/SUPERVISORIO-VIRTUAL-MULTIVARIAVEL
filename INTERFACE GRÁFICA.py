from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

img = ImageTk.PhotoImage(Image.open("imagens/arduino.png"))

class Application():
    def __init__(self):
        self.root = root
        self.tela1()
        self.frames_da_tela1()
        self.botoes()
        root.mainloop()

    def tela1(self):
        self.root.title("SVM - Supervisório Virtual Multivariável")
        self.root.geometry("700x600")
        self.root.configure(background = "#ACCBFF")
        self.root.resizable(False, False)

    def frames_da_tela1(self):
        self.frame1 = Frame(self.root, background = "#E1E1E1")
        self.frame1.place(relx=0.02, rely= 0.02, relwidth=0.96, relheight=0.96)
    
    def botoes(self):
        #botão Iniciar
        self.bt_init = Button(self.frame1, text = "Iniciar", background="white")    
        self.bt_init.place(relx=0.32,rely=0.90,relwidth=0.16,relheight=0.05)  
        #botão Fechar
        self.bt_close = Button(self.frame1, text = "Fechar", background="white")
        self.bt_close.place(relx=0.48,rely=0.90,relwidth=0.16,relheight=0.05)



           


Application()
