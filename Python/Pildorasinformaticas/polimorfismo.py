import os
os.system('cls')

""" polimorfismo es la capacidad de que varios objetos al usar el mismo metodo tengan resultado diferentes
ya lo vimos con herencia y es medio al pepe esto pero hay una idea implementada que está b  """


class coche():
    def moverse(self):
        print("me muevo con mis 4 ruedas")


class moto():
    def moverse(self):
        print("me muevo con mis 2 ruedas")


class camion():
    def moverse(self):
        print("me muevo con mis 6 ruedas")


coche = coche()
moto = moto()
camion = camion()

coche.moverse()
moto.moverse()
camion.moverse()

print("\n---------------------Polimorfismo------------------------\n")


def desplazarse(vehiculo):
    vehiculo.moverse()


desplazarse(moto)
desplazarse(coche)

# desplazarse(camion())
