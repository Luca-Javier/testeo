import os
os.system('cls')


class vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print("Marcha:", self.enMarcha, "\nModelo:", self.modelo, "\nMarca:", self.marca,
              "\nAcelerando:", self.acelerar, "\nfrenando:", self.frenar, "\n")


""" No se podia pasar metodos por el class porque es para la herencia  """


class moto(vehiculo):
    hcaballito = ""

    def caballo(self):
        self.hcaballito = "Estoy haciendo el caballito"
    """ Ahora el estado muestra si hago el caballito, solo en la moto """

    def estado(self):
        print("Marcha:", self.enMarcha, "\nModelo:", self.modelo, "\nMarca:", self.marca,
              "\nAcelerando:", self.acelerar, "\nfrenando:", self.frenar, "\n", self.hcaballito, "\n")


v = vehiculo("Honda", "CBR")
moto = moto("huawei", "C500")
v.estado()
moto.caballo()
moto.estado()


""" class quad(moto):
    ruedas = 4 """


# Seguro se puede y lo vemos despues
""" q = quad("Toyota", "EHH")
q.estado() """


class Velectricos():
    bateria = "cargada"

    def __init__(self, ruedas):
        # self.bateria = "cargada"
        self.ruedas = ruedas

    def btChek(self):
        print("La bateria está", self.bateria)

    def descargar(self):
        self.bateria = "descargada"


""" heredo dos clases pero yo tengo un constructor en cada una. Para saber a cual de los 
constructores tengo que pasarle los parametros que me pide, tengo que ver y fijarme el primero
que declare dentro de la class bicielectrica. vehiculo en este caso """

""" esto es herencia multiple y no muchos lenguajes lo tienen """


class biciElectrica(vehiculo, Velectricos):
    pass


print("Mi bici:\n")
bici = biciElectrica("BMX", "X3000")
""" OHHH, da error porque bateria la crea el constructor, ahora la voy a pasar a la clase """
bici.btChek()
bici.estado()
""" esto se soluciona con super y lo vemos en herencia_2 """
