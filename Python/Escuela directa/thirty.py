""" un string es una cadea de texto, o sea "hola" tiene la h en ell indice 1, o el 2, l el 3 """
from cgitb import text
from re import T


texto = "hola"

print(texto[1])
print(texto[-1])
""" el 0 es la primer letra, siempre. Pero -1 es la ultima """
print(texto[-3])
print(texto.index("l"))
print(texto[texto.index("l")])
# print(texto[texto.index("L")]) error por mayuscula
textoo = "Esta es una prueba"
print("La palabra prueba comienza en la posicion " + str(textoo.index("prueba")))
""" si no se tuviera que usar el string, no huiera andado el print anterior dentro del array """
print("La primera 'a' está en la posición " + str(textoo.index("a")))
""" index busca de izquierda a derecha y choca con la primera que encuentra """
print("La primera 'a' está en la posición " + str(textoo.index("a", 4)))
""" el segundo valor es donde empieza a hacer la busqueda. Si hay una a en la posicion 3 y 
empezamos a buscar en el 3, encuentra esa nomas """
#print("La primera 'a' está en la posición " + str(textoo.index("a", 4, 10)))
""" busca desde la posicion 4 hasta la 10. NO es que empieza en la posicion 4 y busca en las
siguiente 10 posiciones. como no encuentra tira ERROR """
print("La primera 'a' está en la posición " + str(textoo.rindex("a")))
""" rindex empieza desde la derecha, el final """
print("\n----------------Sub-strings-----------------")
texto = "ABCDEFGHIJKLM"
print(texto[2:5])
""" muestro el 2 hasta el 5 sin inluirlo. O sea muestro hasta el 4 """
print(texto[:5])
""" muestra todo hasta el 5 """
print(texto[2:10:2])
""" empieza del 2 y va tomando cada 2 caracteres hasta llegar al 10. Cuando seleccionamos cada
2 caracteres no se empieza a contar desde el 0 """
print(texto[::2])
""" todo pero tomando cada 2 """
print(texto[::-2])
""" empieza de la derecha """
print("\n-------------------Metodos de string---------------")
""" Vamos a ver 6 metodos de string, pero hay 30 """
texto = "Este es el texto de Federico"

print(texto.upper())
print(texto.lower())
print(texto.split())
print(texto.split()[1])
print(texto.split("t"))

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
""" en medio de cada elemento inserto mi variable e, que es un espacio """
print(e)
print(texto.find("t"))
print(texto.find("texto"))
print(texto.find("z"))
""" la diferencia entre find y index es que si find no encuentra lo buscado devuelve un "-1" """
print(texto.replace("Federico", "Javier"))

print("\n----------Propiedades de string---------------")
""" los string no pueden cambiar.
los string se pueden concatenar. No se pueden sumar pero si se pueden multiplicar """
nombre = "Carina"
# nombre[0] = "K"  # DA ERROR
nombre = "Karina"
""" como el string en inmutable no lo puedo cambiar, solo puedo cambiar la variable """
print(nombre)
n1 = "Kari"
n2 = "na"
print(n1 + n2*5)

""" salto de linea """
poema = """Mil pequeños peces blanco 
como si hirviera 
el color del agua"""
print(poema)
""" con 3 comillas puedo hacer saltos de linea  """

""" me fijo si agua está en poema """
print("agua" in poema)
print("sol" not in poema)
print("agua" not in poema)

print("\n---------------Listas(arrays)----------------")
""" puedo anidar array (tener arrays dentor de arrays) y aplicarlos todos los metodos de strings """
lista = ["a", "b", "c"]
lista2 = ["hola", 55, 66.5]
print(lista)
print(type(lista))
print(len(lista))
""" muestra como si fuera una lista """
print(lista + lista2)
""" con los arrays si puedo alterar los elementos """
lista[0] = "A"
print(lista)
lista.append("d")

""" DUDA: por que este si es un metodo, que cambia algo, pero no devuelve nada cuando los otros
metodos podia ponerlos dentro del print de una """
print(lista.append("d"))

"""  """
lista.append("e")
print(lista)
""" elimina el ultimo elemento """
eliminado = lista.pop()
print(lista)
print(f"Elimine la {eliminado}")

lista = ['b', 'c', 'a', 'e', 'd']
lista2 = [13, 7, 23, 6, 68, 3, 3, 67]
lista.sort()
lista2.sort()
""" ordena """
print(lista)
print(lista2)
""" LA DUDA DE ARRIBA
RTA: cuando hacemos un  """
print(lista.sort())
none = lista.sort()
print(none)
""" muestra "none". O sea que el metodo no devuelve nada y esta resultado no sirve de nada
guardarlo. O sea que no es nulo, tampoco 0, es nada. Como hace algo pero no devuelvo nada,
almaceno nada  """

""" o sea que esto es al pedo """
lista = [13, 7, 23, 6, 68, 3, 3, 67]
lista_modified = lista.sort()
print(lista_modified)
print(lista)

""" al reves """
lista.reverse()
print(lista)

print("\n----------Diccionarios----------------")
dic = {'c1': 'valor1', 'c2': 'valor2',
       'c3': 'valor3', 'c4': 'valor3', 'c2': 'valor5'}
""" pueden haber valores repetidos, pero no llaves/claves repetidas """
print(type(dic))
print(dic)
print(dic['c3'])
print(dic['c4'])
""" bueno, si pueden haber llaves repetidas pero la ultima sobrescribe las anteriores """
print(dic['c2'])
cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla': 1.76}
print(cliente['apellido'])

dic = {'c1': 51, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['s1'])

""" EJERCICIO: IMPRIMIR LA "e" EN MAYUSCULA """
dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic = {1: 'a', 2: 'b'}
print(dic[1+1])
dic[3] = 'c'  # AHHH, podría agregar todos los valores así pero es mas rapido con las {}
print(dic[3])
dic[3] = 'kk'
print(dic[3])

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic)
""" con print items vemos que 
dict_items([(1, 'a'), (2, 'b'), (3, 'kk')]) 
y lo que está en parentesis son tuplas"""

""" el valor no me lo toma, pero la llave si """
print('a' in dic)
print(1 in dic)
print("\n----------------Tuplas-------------")
""" ocupan menos memoria, o sea mas eficiencia y son inmutables """
tup = (1, 2, 3, 4)
print(type(tup))
tup = 1, 2, 3, 4  # sin parentesis, medio feo
print(type(tup))

print(tup[-2])  # el 1 es el 0

# tup[0] = 5 #no pibe, un tup es ininmutable
# print(tup[0])
tup = 1, 2, (10, 20), 4
print(tup[2])
print(tup[2][0])

tup = list(tup)
print(type(tup))
tup[0] = 50
print(tup[0])

tup = tuple(tup)
print(type(tup))

""" esto se puede hacer con listas y diccionarios, pero tienen que tener la misma cantidad e elementos """
t = (1, 2, 3)
x, y, z = t
#x, y, z, a = t
#x, y = t
print(x, y, z)
print(y)

t = 1, 2, 3, 1
print(len(t))
""" cuantos 1 hay """
print(t.count(1))
""" posicion del 2 """
print(t.index(2))

print("\n------------------Sets---------------")
""" tiene que almacenar un conjunto, solo uno(que no sea tup) y no tienen datos repetidos """
#mi_set = set(1, 2, 4)
#mi_set = set([1, 2, [5, 6]])
mi_set = set([1, 2, 3, 4, 5])
mi_set = set((1, 2, 3, 4, 5))  # no importa la llave pero tiene que tener
#mi_set = set({1, 2, 3, 4, 5, [1, 2]})
mi_set = set({1, 2, 3, 4, 5})
print(type(mi_set))
print(mi_set)
# print(mi_set[0]) #no se les puede modificar ni mostrar 1
mi_set = set({1, 2, 3, 4, 2, 3, 1, 1, 1, 1, 1, 1, 1, 3, 2, 5, 2, 3, 5, 4, 4})
print(mi_set)

mi_set = set({1, 2, 3, 4, 2, 3, 1, 1, 1, 1, 1, 1,
             1, 3, (55, 66, 77), 5, 2, 3, (55, 66, 77), 4, 4})
print(mi_set)

mi_set = set({1, 2, 3, 4, 2, 3, 1, 1, 1, 1, 1, 1,
             1, 3, (55, 66, 77), 5, 2, 3, (55, 666, 77), 4, 4})
print(mi_set)
""" al cambiar un elemento de la tupla, ya no es la misma """
print(2 in mi_set)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
#s3 = s1 + s2
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.add(2)
print(s1)  # ya existe

# s1.remove(7)
""" como no hay 7, da error eliminarlo """
s1.discard(7)
""" con discard lo descarto, es como eliminar pero no da error. remove es obsoleto creo """
s1.remove(2)
print(s1)

sorteo = s1.pop()  # elimina uno random
print(sorteo)
print(s1)

print("\n----------------Booleanos-------------")
""" los bool´s pueden tener true y false. Pero también pueden contener una operacion que los genere """
my_bool = True
my_bool = False
print(my_bool)
print(type(my_bool))
""" Si uso operadores (yo le llamos condicionales) tengo como resultado true o false de la condicion """
my_bool = 5 > 4
print(my_bool)

lista = (1, 2, 3)
my_bool = 2 in lista
print(my_bool)

my_bool = bool(5 > 6)
print(my_bool)
