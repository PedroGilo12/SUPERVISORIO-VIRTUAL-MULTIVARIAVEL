import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

fig=plt.figure()
gráfico=fig.add_subplot(111)

start=time.time()

xs=[]
ys=[]

x = 1
y = 2

xs.append(x)
ys.append(y)
def atualiza(i):
    #gráfico.clear()
    gráfico.plot(xs,ys,"-o")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valor digitado")
    plt.title("Valor digitado em função do tempo")
    ys.clear()

#threading.Thread(target=grafic).start()
a=animation.FuncAnimation(fig, atualiza, interval=1)
plt.show()