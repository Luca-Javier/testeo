import pickle
import os

os.system('cls')


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva que se llama", self.nombre)

    def __str__(self) -> str:
        return f"{self.nombre} {self.genero} {self.edad}"


class listaPersonas:
    personas = []

    def __init__(self) -> None:
        listaDePersonas = open("savePersonas", "ab+")  # el + para leer
        """ si con el load agarramos un archivo vacío sale error. Va a pasar la primera vez que ejecutemos el codigo """
        try:
            listaDePersonas.seek(0)
            self.personas = pickle.load(listaDePersonas)
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del listaDePersonas

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.__guardarPersonas()

    def mostrarPersonas(self):
        for pp in self.personas:
            print(pp)

    def __guardarPersonas(self):
        # creo que usamos write porque lo va a escribir siempre que creemos una
        # ! Si pongo ab se agrega hasta el infinito
        listaDePersonas = open("savePersonas", "ab")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del listaDePersonas


miLista = listaPersonas()
""" p = Persona("Sandra", "mujer", 29)
miLista.agregarPersonas(p)
p = Persona("Mariana", "mujer", 19)
miLista.agregarPersonas(p)
p = Persona("Juanca", "hombre", 39)
miLista.agregarPersonas(p) """
""" p = Persona("Nuevo", "hombre", 18)
miLista.agregarPersonas(p) """
""" p = Persona("nuevin", "hombre", 20)
miLista.agregarPersonas(p) """
miLista.mostrarPersonas()
print(miLista.personas)
print("\n---------------Dentro del archivo---------------------\n")
check = open("savePersonas", "rb")
print(pickle.load(check))
""" por que a este no le hace falta el seek 0 y al primero si?? """
