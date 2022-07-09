import math


def evaluaEdad(edad):
    if edad < 0:
        """ podemos elegir que error mandarle y con un mensaje """
        #raise TypeError("No se permiten edades negativas")
        """ sale nameError """
        raise myError("Error echo por mi")

    if edad < 20:
        return "Eres joven"
    elif edad < 40:
        return "Eres maduro"
    elif edad < 100:
        return "Warning"


print(evaluaEdad(30))
print(evaluaEdad(10))
# print(evaluaEdad(-10))
""" vamos a crear nuestra excepsion, porque no es logico que me pongan que tienen años negativos """


def calcularRaiz(num):
    if num < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num)


try:
    print(calcularRaiz(int(input("Numero para calcular raiz: "))))
    """ capturo el error que yo mismo lanze """
except ValueError as ErrorNumeroNegativo:
    print("Numero negativos no")
