""" interfaces grafias o GUI (graphic user interface) """
""" el codigo de la librería sería la raiz, luego la interfaz es el frame y dentro los widgets """
""" os.system('cls') """

from tkinter import *
raiz = Tk()

raiz.title("Ventana test")
""" es para que las dimensiones se pueden redimensionar, cambiar, agrandar y achicar """
""" pide 2 booleanos y yo le puedo pasar 1, 0, false, true """
raiz.resizable(0, False)

raiz.iconbitmap("assets/favicon-16x16-1.png")

raiz.geometry("650x350")

raiz.config(bg="purple")


raiz.mainloop()  # hace un bucle infinito que está desplegando la interfaz constantemente. Gracias a esto está a la escucha de eventos
""" si cambio la extencion a pyw ya no hace falta abrir la consola, apreto el archivo y la ventana se abre """
