from tkinter import *
import os


os.system('cls')
# * Variables
btnHeight = "2"
btnWidth = "5"
border = "borderwidth=3, relief='ridge'"
chauWrited = False


# * Codigo
r = Tk()
r.resizable(width="0", height="0")

f = Frame(r, bg="grey56")
f.grid(row="0", column="0", columnspan="4")

# * Funciones
canalCalc = StringVar(r)
canalRegistro = StringVar(r)


def escribir(caract):
    estaba = calc.get()
    canalCalc.set(estaba + caract)
    print(chauWrited)


def igualar():
    pass


def borrar(accion):
    if accion == "C":
        canalCalc.set("")
        canalRegistro.set("")
    else:
        oldCalc = list(calc.get())
        cant = len(oldCalc) - 1
        oldCalc[cant] = ""
        oldCalc.remove("")
        newCalc = "".join(oldCalc)
        canalCalc.set(newCalc)


def sumar():
    estaba = calc.get()
    canalRegistro.set(estaba + "+")
    chauWrited = True

    return chauWrited  # ? para que lo lea otro metodo


print(chauWrited)
# * Shell 5cxr5
# * Fila inputs
calcRegistro = Entry(f, textvariable=canalRegistro, justify="right")
calcRegistro.grid(row=0, column=0, columnspan=4, sticky="ew")
calc = Entry(f, textvariable=canalCalc, justify="right")
calc.insert(0, "0")
calc.grid(row=1, column=0, columnspan=4, sticky="ew")

# * Primero fila con botones de borrar
btnBorrar_all = Button(f, text="C", width=btnWidth,
                       height=btnHeight, command=lambda: borrar("C"))
btnBorrar_all.grid(row="2", columnspan=3, sticky="ew")
btnBorrar_one = Button(f, text="X", width=btnWidth,
                       height=btnHeight, command=lambda: borrar("X"))
btnBorrar_one.grid(row="2", column="3")

# * Fila 1
btn7 = Button(f, text="7", width=btnWidth,
              height=btnHeight, command=lambda: escribir("7"))
btn7.grid(row="3", column="0")
btn8 = Button(f, text="8", width=btnWidth, height=btnHeight,
              command=lambda: escribir("8"))
btn8.grid(row="3", column="1")
btn9 = Button(f, text="9", width=btnWidth, height=btnHeight,
              command=lambda: escribir("9"))
btn9.grid(row="3", column="2")
btnDiv = Button(f, text="/", width=btnWidth, height=btnHeight,
                command=lambda: escribir("/"))
btnDiv.grid(row="3", column="3")

# * Fila 2
btn4 = Button(f, text="4", width=btnWidth, height=btnHeight,
              command=lambda: escribir("4"))
btn4.grid(row="4", column="0")
btn5 = Button(f, text="5", width=btnWidth, height=btnHeight,
              command=lambda: escribir("5"))
btn5.grid(row="4", column="1")
btn6 = Button(f, text="6", width=btnWidth, height=btnHeight,
              command=lambda: escribir("6"))
btn6.grid(row="4", column="2")
btnMult = Button(f, text="x", width=btnWidth,
                 height=btnHeight, command=lambda: escribir("x"))
btnMult.grid(row="4", column="3")

# * Fila 3
btn1 = Button(f, text="1", width=btnWidth, height=btnHeight,
              command=lambda: escribir("1"))
btn1.grid(row="5", column="0")
btn2 = Button(f, text="2", width=btnWidth, height=btnHeight,
              command=lambda: escribir("2"))
btn2.grid(row="5", column="1")
btn3 = Button(f, text="3", width=btnWidth, height=btnHeight,
              command=lambda: escribir("3"))
btn3.grid(row="5", column="2")
btnRest = Button(f, text="-", width=btnWidth,
                 height=btnHeight, command=lambda: escribir("-"))
btnRest.grid(row="5", column="3")

# * Fila 4
btnSuma = Button(f, text="+", width=btnWidth,
                 height=btnHeight, command=sumar)
btnSuma.grid(row="6", column="3")
btn0 = Button(f, text="0", width=btnWidth, height=btnHeight,
              command=lambda: escribir("0"))
btn0.grid(row="6", column="1")
btnComa = Button(f, text=",", width=btnWidth,
                 height=btnHeight, command=lambda: escribir(","))
btnComa.grid(row="6", column="0")
btnIgual = Button(f, text="=", width=btnWidth,
                  height=btnHeight, command=igualar)
btnIgual.grid(row="6", column="2")


r.mainloop()
