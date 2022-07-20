from tkinter import *

r = Tk()
f = Frame(r,)
f.pack()

""" PhotoImage solo soporta gif, png, etc. Y por alguna razon no anda con rutas que no sean la
misma donde está el archivo """
img = PhotoImage(file='/assets/favicon-16x16-1.png/')

l = Label(image=img)
l.pack()

r.mainloop()
