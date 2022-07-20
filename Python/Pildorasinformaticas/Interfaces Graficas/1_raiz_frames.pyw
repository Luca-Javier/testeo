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

miFrame = Frame()

miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="600", height="300")
""" la raiz se ajusta al tamaño del frame, o sea que no hace falta darle un tamaño a la raiz.
Pero si tenemos diferentes tamaños vemos que el frame se empieza a construir desde arriba y el centro """
raiz.resizable(1, 1)
miFrame.pack(side="bottom")  # ?Ahora empieza desde abajo tipo constrain
miFrame.pack(side="left", anchor="n")  # le damos puntos cardinales
""" es una verga el anchor, promete tipo puntos cardinales pero el side tiene prioridad y por default es top
y tiene además un center, este side implicito supero al anchor. El anchor por si solo no sirve, solo complmentea
el side """
miFrame.pack(fill="y", expand="1")  # fill: para que rellene la raiz. Tiene both
# expand: para que se centre responsivamente

miFrame.config(relief="solid", bd="35")  # borde

miFrame.config(cursor="pirate")

raiz.mainloop()  # hace un bucle infinito que está desplegando la interfaz constantemente. Gracias a esto está a la escucha de eventos
""" si cambio la extencion a pyw ya no hace falta abrir la consola, apreto el archivo y la ventana se abre """

""" Me empiezo a dar cuenta de que todo lo que hago en css, html, php, js, es simplemente una
forma de hacerlo, la forma web. Pero estoy seguro de que con python puedo hacer una app y que 
haga por EJ todo lo de regencia """
