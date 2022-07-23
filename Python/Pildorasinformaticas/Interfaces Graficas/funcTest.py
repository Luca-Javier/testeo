from tkinter import *

r = Tk()
r.config(width=200, height=200)
""" es como que StringVar es un canal y cuando usa una funcion agarro el ultimo valor que pase """
use = StringVar(r)


def poner():
    write = pre.get()
    use.set(write)


btn = Button(r, text="enviar", command=poner)
ing = Entry(r, textvariable=use)
pre = Entry(r)

ing.grid(row=0, column=1)
btn.grid(row=0, column=0)
pre.grid(row=1, column=1)

r.mainloop()
