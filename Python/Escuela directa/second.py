
""" con second me refiero a segundo archivo y segundo día según el video """
""" TIPOS DE DATOS
anoto los diferentes y los nuevos """
"""
String (str)
listas (lst)  =  arrays  con cualquier tipo de dato dentro ["sal",1,-3,4.5]
diccionarios (dic)  =  arrays asociativos {'color':'rojo','arte':'cine'}. No tiene orden o indice
tuples/tuplas (tup)  =  array const, o sea no cambia('lun','mar',mie','jue'). Creo que no
cambian las posiciones, pero si puedo agregar y sacar
sets (set)  =  arrays sin datos repetidos{'a','b','c','d'}
"""
""" las variables no pueden empezar con numero, pero si contener. No pueden tener simbolos o
palabras clave 
"""


from ast import Str
num_int = 1
num_int = num_int-0.5
print(num_int)

edad = "30"  # input("\nDime tu edad: ")
print("tu edad es " + edad)
#nueva_edad = 1 + edad

""" como el 1 no es un string, no se concatena y es error. La edad es un string """
""" hay 2 tipos de conversiones de datos.
Implicitas: sería las que hace python solo, tipo miDato = 1 y despues lo igualo a un string
Explicita: cuando nosotros, el usuario, cambia la variable con codigo """
""" conversion implicita EJ: """

""" num1 = 20
num2 = 0.5
num1 = num1 + num2
print(type(num1)) """
""" num1 que era int ahora es float sin haber echco nada """

""" explicitas: """
edad = int(edad)
nueva_edad = 1 + edad
#print("Vas a cumplir " + nueva_edad)
""" esto está mal porque nueva_edad es un numero, y cuando sumamos un numero con un string 
hay error """
print(nueva_edad)
# print(Nueva_edad) es key sensitive
print("Vas a cumplir: " + str(nueva_edad))


""" test de redondeo con int() """
print("\n-----------test redondeo--------------")
num11 = 0
# num22 = .5 #esto vale
num22 = .999  # redondea para abajo
print(int(num11 + num22))
print("si paso una suma con decimales se redondea al piso")

""" format. Para formatear cadenas y no tener que transformar cada parametro en string puedo formatear """
print("\n---------------FORMAT----------------------")
frase1 = "auto rojo"
frase2 = "256"
print("Mi {} pesa {}kg".format(frase1, frase2))
print(f"Mi {frase1} pesa {frase2}kg")
""" no puedo hacer un print de {} """

print("\n------------------Operadores matematicos----------------")
x = 6
y = 2
z = 7
print(f"{x} mas {y} es igual a {x + y}")
print(f"{x} menos {y} es igual a {x - y}")
print(f"{x} por {y} es igual a {x * y}")
print(f"{x} dividido {y} es igual a {x / y}")
""" dividir al piso es que si da con decimal, lo redondeo para abajo """
print(f"{z} dividido al piso de {y} es igual a {z//y}")
""" modulo/resto """
print(f"{z} modulo de {y} es igual a {z%y}")
""" potencias """
print(f"{z} elevado a la {y} es igual a {z**y}")
""" raiz """
print(f"la raiz cuadrada de {25} es {25**0.5}")
print(f"la raiz cuadrada aproximada de {8} es {int(8**0.5)}")
print(f"{7} + {.5} se redondea a {round(7 + .5)}")
print(f"{7} + {.49} se redondea a {round(7 + .49)}")
print(f"Te muestro solo 3 decimales{round(95.6666666666666666666,3)}")

print("\n------------------Proyecto 2----------------")
nombre = input("Decime tu nombre: ")
ganancia = int(input("Cuanto ganaste?: "))

print(f"Hola {nombre}, te corresponde ${round(ganancia / 100 * 13,2)}")
