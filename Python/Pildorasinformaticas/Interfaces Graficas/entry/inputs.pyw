from tkinter import *

from pyparsing import col

r = Tk()
f = Frame(r, width="500", height="500")
f.pack()

input = Entry(f).place(x="100", y="100")
nombreLabel = Label(f, text="Nombre:").place(
    x="100", y="100")   # ?No los sobrepone, los pone al lado

""" QUE GRANDE GRID """
input2 = Entry(f).grid(row=1, column=2)
nombreLabe2 = Label(f, text="Nombre2:").grid(row=1, column=1)

input3 = Entry(f).grid(row=2, column=2)
nombreLabe3 = Label(f, text="Apellido:").grid(
    row=2, column=1)

input4 = Entry(f).grid(row=3, column=2)
nombreLabe4 = Label(f, text="Direccion de casa:").grid(row=3, column=1)
""" es como el pack, hace que la raiz se ajuste a su tamaño """
""" las grids por default tienen un justify center. O sea que la label direccion al ser mucho mas
larga las otras quedan centradas. Para ponerlas a la izquierda usamos sticky con puntos cardinales """

input5 = Entry(f).grid(row=4, column=2)
nombreLabe5 = Label(f, text="Nombre2:").grid(row=4, column=1, sticky="e")

input6 = Entry(f).grid(row=5, column=2)
nombreLabe6 = Label(f, text="Apellido:").grid(row=5, column=1, sticky="w")

""" padding """
input7 = Entry(f)
# si pongo .grid ahi cuando lo creo, despues config salta error

input7.grid(row=6, column=2)
input7.config(fg="red", justify="center")

nombreLabe7 = Label(f, text="Padding:").grid(
    row=6, column=1, padx="100", pady="40")

""" Como la raiz se ajusta a lo que ocupen los widgetss. Apenas cuando ya exista la cordenada
del primero que cree, recien ahi aparece y me hace quilombo """

input8 = Entry(f)
# si pongo .grid ahi cuando lo creo, despues config salta error

input8.grid(row=7, column=2)
input8.config(show="*")
input8.config(show="ñl")  # Solo la primera letra

nombreLabe8 = Label(f, text="Password:").grid(row=7, column=1)
r.mainloop()
