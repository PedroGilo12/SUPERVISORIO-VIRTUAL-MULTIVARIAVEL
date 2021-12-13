import threading
import time
import Interface
import Teste
import serial.tools.list_ports

def funcao():
	while 1:
		print("Running")
		run = Interface.init1.get()
		if run == 1:
			Variavel1 = Interface.Var1.get()
			Variavel2 = Interface.Var2.get()
			Variavel3 = Interface.Var3.get()

			Pino1 = Interface.Pin1.get()
			Pino2 = Interface.Pin2.get()
			Pino3 = Interface.Pin3.get()

			print(f'Channel 1: Pino A{Pino1}, Variável {Variavel1}')
			print(f'Channel 2: Pino A{Pino2}, Variável {Variavel2}')
			print(f'Channel 3: Pino A{Pino3}, Variável {Variavel3}')
			Interface.resumeInterface()

Teste.runSelectSerial()
threading.Thread(target=funcao).start()
Interface.runInterface()
	