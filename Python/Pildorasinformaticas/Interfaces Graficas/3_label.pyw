from tkinter import *

raiz = Tk()
f = Frame(width="500", height="500")
raiz.title("Agregando Widgets")
f.pack()

label1 = Label(text="Hola mi ente", fg="cyan", font=(
    "Raleway", 21))  # puedo poner .place() acá
# label1.pack()

""" cuando creo un frame o un label, puedo poner el contenedor padre. No es necesario pero calculo
que luego al usar 2 frames si o simplemente es una buena practica. El punto es que cuando lo hacemos el
ultimo elemento en usar pack() hace que la raiz se ajuste a el mismo """
label1.place(
    x="100", y="100")  # tipo left y top. EL default es casi pegado, un margin fino

""" img = PhotoImage(file="/assets/R.jpg") """
img2 = PhotoImage(file="favicon-16x16.png", width="400", height="400")
label2 = Label(image=img2).place(x="100")
raiz.mainloop()

""" Me doy cuenta de que si el día de mañana no hago desarrollo web, no fue al pedo porque aprendí
tips para maquetar, diseñar y todo eso se aplica sea la web o una app """
