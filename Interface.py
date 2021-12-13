from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os
import serial.tools.list_ports

root = Tk()

root.iconbitmap('imagens/icone.ico')

Var1 = StringVar()
Var2 = StringVar()
Var3 = StringVar()

Pin1 = IntVar()
Pin2 = IntVar()
Pin3 = IntVar()


ArdUno = IntVar()
ArdNano = IntVar()

init1 = IntVar()
init1.set(0)

AnSel = IntVar()
AnSel.set(-1)

Var_Sel = StringVar()
Var_Sel.set("0")

img_uno = ImageTk.PhotoImage(Image.open("imagens/arduino_uno_small.png"))
img_nano = ImageTk.PhotoImage(Image.open("imagens/arduino_nano_small.png"))
img_anm1 = ImageTk.PhotoImage(Image.open("imagens/animation1.gif"))

class Interface():

    def __init__(self):
        self.root = root
        self.tela1()
        self.frames_da_tela1()
        self.widgetsframe1()
        self.widgetsframe2()
        self.widgetsframe3()
        self.widgetsframe0()
        root.mainloop()

    def tela1(self):
        self.root.title("SVM - Supervisório Virtual Multivariável")
        self.root.geometry("800x600")
        self.root.configure(background = "#ACCBFF")
        self.root.resizable(False, False)

    def frames_da_tela1(self):
        self.frame0 = Frame(self.root, background = "#E1E1E1")
        self.frame0.place(relx=0.02, rely= 0.29, relwidth=0.37, relheight=0.69)

        self.frame1 = Frame(self.root, background = "#E1E1E1")
        self.frame1.place(relx=0.41, rely= 0.29, relwidth=0.57, relheight=0.69)

        self.frame2 = Frame(self.root, background = "white")
        self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.12)

        self.frame3 = Frame(self.root, background = "white")
        self.frame3.place(relx=0.02, rely=0.14, relwidth=0.96, relheight=0.12)

    def widgetsframe0(self):
        self.titlef0 = Label(self.frame0,text= "SELECIONE AS VARIÁVEIS MONITORADAS", background = "#E1E1E1")
        self.titlef0.pack()

        # FRAME DA VARIÁVEL 1
        self.subframe0 = Frame(self.frame0, background = "white")
        self.subframe0.place(relx=0, rely=0.12, relwidth=1,relheight=0.20)

        self.Tvariavel1 = Label(self.subframe0, text = "VARIÁVEL 1", background = "white")
        self.Tvariavel1.place(relx=0.01, rely=0.01)

        self.An1Sel = Button(self.subframe0, text= "Selecione a porta analógica: ", command = self.An1Select)
        self.An1Sel.place(relx=0.01, rely=0.25)

        self.var1Sel = Button(self.subframe0, text= "Selecione a variável: ", command = self.var1Select)
        self.var1Sel.place(relx=0.01, rely=0.6)

        # FRAME DA VARIÁVEL 2
        self.subframe1 = Frame(self.frame0, background = "white")
        self.subframe1.place(relx=0, rely=0.42, relwidth=1,relheight=0.20)

        self.Tvariavel2 = Label(self.subframe1, text = "VARIÁVEL 2", background = "white")
        self.Tvariavel2.place(relx=0.01, rely=0.01)

        self.An1Sel = Button(self.subframe1, text= "Selecione a porta analógica: ", command = self.An2Select)
        self.An1Sel.place(relx=0.01, rely=0.25)

        self.var1Sel = Button(self.subframe1, text= "Selecione a variável: ", command = self.var2Select)
        self.var1Sel.place(relx=0.01, rely=0.6)

        # FRAME DA VARIÁVEL 3
        self.subframe2 = Frame(self.frame0, background = "white")
        self.subframe2.place(relx=0, rely=0.72, relwidth=1,relheight=0.20)

        self.Tvariavel3 = Label(self.subframe2, text = "VARIÁVEL 3", background = "white")
        self.Tvariavel3.place(relx=0.01, rely=0.01)

        self.An1Sel = Button(self.subframe2, text= "Selecione a porta analógica: ", command = self.An3Select)
        self.An1Sel.place(relx=0.01, rely=0.25)

        self.var1Sel = Button(self.subframe2, text= "Selecione a variável: ", command = self.var3Select)
        self.var1Sel.place(relx=0.01, rely=0.6)

    def widgetsframe1(self):
        #botão Iniciar
        self.bt_init = Button(self.frame1, text = "Iniciar", background="white", command = self.init)    
        self.bt_init.place(relx=0.67,rely=0.95,relwidth=0.16,relheight=0.05)  
        #botão Fechar
        self.bt_close = Button(self.frame1, text = "Fechar", background="white", command = self.close)
        self.bt_close.place(relx=0.84,rely=0.95,relwidth=0.16,relheight=0.05)

        #self.imagem = Label(self.frame1, text = "IMAGEM", image = img_uno, background = "#E1E1E1")
        #self.imagem.place(relx=0.25,rely=0.01,relwidth=0.50,relheight=0.75)

    def widgetsframe2(self):
        self.ft = tkFont.Font(family='Arial',size=16)
        self.title = Label(self.frame2, text = "SUPERVISÓRIO VIRTUAL MULTIVARIÁVEL", font = self.ft, background = "white").place(rely = 0.2, relx = 0.225)

    def widgetsframe3(self):
        self.menu_text = Label(self.frame3, text = "SELECIONE O HARDWARE UTILIZADO", background = "white")
        self.menu_text.pack()

        self.marker_uno = Checkbutton(self.frame3, text = "Arduino uno", variable = ArdUno, onvalue = 1, offvalue = 0, command = self.ArduinoUnoMarker)
        self.marker_uno.place(relx = 0.25, rely=0.4, relwidth=0.25, relheight=0.30)

        self.marker_nano = Checkbutton(self.frame3, text = "Arduino nano", variable = ArdNano, onvalue = 1, offvalue = 0, command = self.ArduinoNanoMarker)
        self.marker_nano.place(relx = 0.50, rely=0.4, relwidth=0.25, relheight=0.30)

    def ArduinoUnoMarker(self):
        self.marker_nano.deselect()
        self.imagem = Label(self.frame1, text = "IMAGEM", image = img_uno, background = "#E1E1E1")
        self.imagem.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

    def ArduinoNanoMarker(self):
        self.marker_uno.deselect()
        self.imagem = Label(self.frame1, text = "IMAGEM", image = img_nano, background = "#E1E1E1")
        self.imagem.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

    def init(self):
        print("Iniciado")
        init1.set(1)

    def close(self):
        self.root.quit()
        self.root.destroy()

    def GeneralSel(self):
        self.frame4 = Frame(self.frame1, background = "white")
        self.frame4.place(relx = 0, rely = 0.75, relwidth=1, relheight = 0.2)
        self.A0 = Checkbutton(self.frame4, text = "A0",variable = AnSel, onvalue = 0, offvalue = 0,).place(relx = 0.1, rely = 0.2)
        self.A1 = Checkbutton(self.frame4, text = "A1",variable = AnSel, onvalue = 1, offvalue = 0,).place(relx = 0.2, rely = 0.2)
        self.A2 = Checkbutton(self.frame4, text = "A2",variable = AnSel, onvalue = 2, offvalue = 0,).place(relx = 0.3, rely = 0.2)
        self.A3 = Checkbutton(self.frame4, text = "A3",variable = AnSel, onvalue = 3, offvalue = 0,).place(relx = 0.4, rely = 0.2)
        self.A4 = Checkbutton(self.frame4, text = "A4",variable = AnSel, onvalue = 4, offvalue = 0,).place(relx = 0.5, rely = 0.2)
        self.A5 = Checkbutton(self.frame4, text = "A5",variable = AnSel, onvalue = 5, offvalue = 0,).place(relx = 0.6, rely = 0.2)
        #print(AnSel.get())

        self.ButtonSelectAn = Button(self.frame4, text = "Selecionar", command = self.PinSelected).place(relx = 0.1, rely = 0.5)

    def An1Select(self):
        self.button = 1
        self.GeneralSel()

    def An2Select(self):
        self.button = 2
        self.GeneralSel()

    def An3Select(self):
        self.button = 3
        self.GeneralSel()

    def GeneralVarSel(self):
        self.frame4 = Frame(self.frame1, background = "white")
        self.frame4.place(relx = 0, rely = 0.75, relwidth=1, relheight = 0.2)

        self.Temp = Checkbutton(self.frame4, text = "Temperatura",variable = Var_Sel, onvalue = "Temperatura", offvalue = "0",).place(relx = 0.1, rely = 0.1)
        self.Umid = Checkbutton(self.frame4, text = "Umidade",variable = Var_Sel, onvalue = "Umidade", offvalue = "0",).place(relx = 0.1, rely = 0.4)
        self.Tens = Checkbutton(self.frame4, text = "Tensão",variable = Var_Sel, onvalue = "Tensão", offvalue = "0",).place(relx = 0.1, rely = 0.7)

        self.bt_varsel = Button(self.frame4, text = "Selecionar", command = self.VarSelected).place(relx = 0.5, rely = 0.7)

    def var1Select(self):
        self.varsel = 1
        self.GeneralVarSel()

    def var2Select(self):
        self.varsel = 2
        self.GeneralVarSel()

    def var3Select(self):
        self.varsel = 3
        self.GeneralVarSel()

    def VarSelected(self):
        if self.varsel == 1:
            Var1.set(Var_Sel.get())
            self.Var1Selected = Label(self.subframe0, text = f"{Var1.get()}").place(relx = 0.45, rely = 0.63, relwidth = 0.30, relheight = 0.30)

        if self.varsel == 2:
            Var2.set(Var_Sel.get())
            self.Var2Selected = Label(self.subframe1, text = f"{Var2.get()}").place(relx = 0.45, rely = 0.63, relwidth = 0.30, relheight = 0.30)

        if self.varsel == 3:
            Var3.set(Var_Sel.get())
            self.Var2Selected = Label(self.subframe2, text = f"{Var3.get()}").place(relx = 0.45, rely = 0.63, relwidth = 0.30, relheight = 0.30)

        Var_Sel.set(" ")
        self.frame4.destroy()

    def PinSelected(self):
        if self.button == 1:
            Pin1.set(AnSel.get())
            self.Pin1Selected = Label(self.subframe0, text = f"A{Pin1.get()}").place(relx = 0.6, rely = 0.23, relwidth = 0.30, relheight = 0.30)

        if self.button == 2:
            Pin2.set(AnSel.get())
            self.Pin2Selected = Label(self.subframe1, text = f"A{Pin2.get()}").place(relx = 0.6, rely = 0.23, relwidth = 0.30, relheight = 0.30)

        if self.button == 3:
            Pin3.set(AnSel.get())
            self.Pin2Selected = Label(self.subframe2, text = f"A{Pin3.get()}").place(relx = 0.6, rely = 0.23, relwidth = 0.30, relheight = 0.30)

        AnSel.set(-1)
        self.frame4.destroy()

def runInterface():
    Interface()

def resumeInterface():
    root.destroy()

