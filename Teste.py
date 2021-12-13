from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os

import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())

root = Tk()

com = StringVar()


class SelectSerial():

    def __init__(self):
    	self.root = root
    	self.tela1()
    	self.frames_tela1()
    	self.widgets_frame0()
    	root.mainloop()

    def tela1(self):
        self.root.title("SVM - Supervisório Virtual Multivariável")
        self.root.geometry("300x300")
        self.root.configure(background = "#ACCBFF")
        self.root.resizable(False, False)

    def frames_tela1(self):
    	self.frame0 = Frame(self.root, background = "white")
    	self.frame0.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    def widgets_frame0(self):
    	x = 1
    	self.title = Label(self.frame0, text="SELECIONE A PORTA SERIAL: ", background = "white").pack()
    	self.lista = Listbox(self.frame0, background = "#E1E1E1")
    	for p in ports:
    		self.lista.insert(x, p)
    		x = x + 1

    	x = 1

    	self.lista.place(relx = 0.1, rely = 0.2, relheight = 0.6, relwidth = 0.8)

    	self.buttonsel = Button(self.frame0, text = "Prosseguir", command = self.selected).place(relx = 0.35, rely = 0.8)

    def selected(self):
    	com.set(self.lista.get(ACTIVE))
    	print(com.get())
    	self.root.quit()
    	self.root.destroy()


def runSelectSerial():
    SelectSerial()
