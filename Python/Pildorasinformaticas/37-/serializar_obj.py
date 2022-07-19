import pickle


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


car1 = vehiculo("Honda", "G300")
car2 = vehiculo("Toyota", "MX5")
car3 = vehiculo("Renault", "Leon")

misCoches = [car1, car2, car3]

guardarCoches = open("cochesGuardados", "wb")
pickle.dump(misCoches, guardarCoches)
guardarCoches.close()

""" borro la variable del codigo. Entiendo que es util pero lo tendria que hacer siempre que cierre
un archivo, no solamente por esto que estoy haciendo acá, serializar """
del guardarCoches

chek = open("cochesGuardados", "rb")
loadCoches = pickle.load(chek)
chek.close()
del chek

for c in loadCoches:
    print(c.estado())
