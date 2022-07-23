from cgitb import text
from tkinter import *
import os

from pyparsing import col
from setuptools import Command

os.system('cls')

r = Tk()
r.config(width="500", height="500")

comentarios = Label(r, text="comentario:").grid(row=0, column=0)
comentarioTxt = Text(r, width=10, height=10)
""" si pongo height 2 es como que ocupe 2 rows """
comentarioTxt.grid(row=0, column=1)

""" le dicemos que a comentarioTxt le ponga un scroll en y """
scrolly = Scrollbar(r, command=comentarioTxt.yview)
""" está a la derecha del text area pero no pegado a la raiz """
scrolly.grid(row=0, column=2)
""" el scroll por default ocupa lo minimo aunque dentro del text area haya mil lineas """
scrolly.grid(sticky="nsew")
""" recien ahora el scroll como que entiende que tiene que mover el text area """
comentarioTxt.config(yscrollcommand=scrolly.set)

rta = StringVar(r)


def btnAccion():
    rta.set("enviado")


btnRta = Entry(r, textvariable=rta).grid(row="1", column="1")

btn = Button(r, text="Enviar", command=btnAccion).grid(row="1", column="0")
""" si uso grid ya no puedo usar pack """


r.mainloop()
