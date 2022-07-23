from tkinter import *
import os

os.system('cls')
r = Tk()
r.config(width="200", height="200")

rowBtn = 3

num1 = Entry(r).grid(row="0", column="2")
num2 = Entry(r).grid(row="1", column="2")


def sumar():
    resultado.set(int(num11.get()) + int(num22.get()))


def multiplicar():
    resultado.set(str(int(num11.get()) + int(num22.get())))


def restar():
    resultado.set(int(num11.get()) + int(num22.get()))


btnSumar = Button(r, text="Sumar", command=sumar).grid(row=rowBtn, column="0")
btnMult = Button(r, text="Multiplicar", command=multiplicar).grid(
    row=rowBtn, column="1")
btnRest = Button(r, text="Restar", command=restar).grid(row=rowBtn, column="2")
rta = Entry(r).grid(row=rowBtn, column="3")

resultado = StringVar(rta)
num11 = StringVar(num1)
num22 = StringVar(num2)

r.mainloop()
