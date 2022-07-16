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
        """ le paso los valores al constructor padre para que los guarde """
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.atiguedad = antiguedad


""" en el otro caso era lo que herede primero, pero ahora no tengo idea """
""" toma el constructor de empleado, pero no podria usar el metodo descripcion """
p1 = empleado(150, 2, "carlos", 44, "new york")
""" Ahora que hice el super si anda """
p1.descripcion()
print("FIN")
""" Al hacer herencia siempre tenemos que pensar EJ: un empleado es siempre una persona. Si la
respuesta es si entonces empeleado puede heredar, pero si una persona no es siempre un empleado """
print(isinstance(p1, empleado))  # devuelve true si p1 es una instancia de empleado
print(isinstance(p1, persona))

""" TEST """


class vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def pr(self):
        print(self.marca, self.modelo)


class Velectricos(vehiculo):
    def __init__(self, ruedas, marca, modelo):
        # self.bateria = "cargada"
        self.ruedas = ruedas
        super().__init__(marca, modelo)

    def prRuedas(self):
        print(self.ruedas)


class test(Velectricos, vehiculo):
    pass


t1 = test(2, "bmx", "honda")
t1.pr()  # ?y al revez??
t1.prRuedas()

""" si ya electricos hereda a vehiculos es al pedo que testt herede los 2. Pero el error viene
a que el constructor acá es vehiculo por estar primero y no tiene sentido porque no puedo hacer
un super a una clase hija, solo a padre. Por eso test no da error """
""" 
?La verdadera DUDA:
si heredo 2 clases que no tienen nada que ver, como les paso a las 2 los constructores?. En
el archivo herencia pasa eso y nos vemos obligados a que electricos herede vehiculo para poder
usar el super. Debe ser eso, ya no hay duda jaja, que boludo
 """


class testt(vehiculo, Velectricos):
    pass


t2 = vehiculo()
