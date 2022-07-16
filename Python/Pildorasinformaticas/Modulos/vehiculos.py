import os
os.system('cls')


class persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre", self.nombre, "\nEdad:",
              self.edad, "\nResidencia:", self.residencia)


class empleado(persona):
    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.atiguedad = antiguedad


p1 = empleado(150, 2, "carlos", 44, "new york")

p1.descripcion()
print(isinstance(p1, empleado))
print(isinstance(p1, persona))


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


class moto(vehiculo):
    hcaballito = ""

    def caballo(self):
        self.hcaballito = "Estoy haciendo el caballito"

    def estado(self):
        print("Marcha:", self.enMarcha, "\nModelo:", self.modelo, "\nMarca:", self.marca,
              "\nAcelerando:", self.acelerar, "\nfrenando:", self.frenar, "\n", self.hcaballito, "\n")


class Velectricos(vehiculo):
    def __init__(self, ruedas, marca, modelo):
        # self.bateria = "cargada"
        self.ruedas = ruedas
        super().__init__(marca, modelo)

    def prRuedas(self):
        print(self.ruedas)


class test(Velectricos, vehiculo):
    pass
