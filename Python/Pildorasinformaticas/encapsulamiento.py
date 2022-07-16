import os
os.system('cls')


class coche():

    def __init__(self):
        self.color = "rojo"
        self.__ruedas = 4
        self.llendo = False

    def arrancar(self, arrancamos):
        self.llendo = arrancamos
        if self.llendo:
            chekk = self.__chek()  # me fijo antes de arrancar si está todo bien. No tiene sentido que me tenga un metodo de fijarme si me tengo que fijar si o si antes de arrancar

        """ pay attention: si pongo de condicion chekk pero llendo es false, nunca creo la variable chekk
        entonces da error. Pero al poner llendo and chekk ya no da error. Es como que chekk al no 
        existir y necesitarlo da error pero como el primero es false tmb tampoco importaba si existia o no.
        O sea que si pongo "or" da error y tambien si pongo chekk antes que llendo (con and) """
        if self.llendo and chekk:
            print("Arrancamos")
        else:
            print("Cuidado")

    def __chek(self):
        print("Realizando chekeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


car = coche()
car2 = coche()

car.arrancar(True)
car2.arrancar(False)

# no tiene sentido hacer un chekk cuando no estemos arrancado. Por eso lo hacemos privado
try:
    print(car.chek())
    print(car.__chek())
except AttributeError:
    print("El metodo es privado")
""" car.estado()
car2.estado()
 """
