from asyncore import read
from io import open

a = open("archivo_txt", "r")

""" solo muesta una porque es como el lector llego al final y ya se queda ahí """
""" cuando escibimos tenemos esta barrita blanca. Es mas facil entender que la barrita se quedó
Al final y hay una manera de moverla """
print(a.read())
print(a.read())

print("el seek mueve la barrita\n")
a.seek(0)
print(a.read())

print("\nempezando en el caracter 11")
a.seek(11)
print(a.read())

print("\nleyendo hasta el caracter 11")
a.seek(0)
print(a.read(11))

print("\nLo que faltó:\n"+a.read())

""" en verdad al archivo tiene 66 pero la posicion 0 es el primer y el que falta """
a.seek(0)
print("el archivo tiene", len(a.read()), "caracteres")

""" para poner la barrita/cursor en el medio hacemos """
""" si yo hago un punto y aparte esos espacios en blanco no se cuentan. De echo valen menos porque
si tengo:

estudiando python
un viernes
porque falto blanco
agregando info

entre python y un viernes. No tengo espacio en blanco. Pero si tengo

estudiando python un viernes

ahora tengo un espacio en blanco en medio, por lo que tengo mas. Lo mas eficiente debe ser
en cada espacio en blanco dar un salto y ocupo menos memoria??"""
a.seek(0)
a.seek(len(a.read())/2)
print("\nLa mitad:\n", a.read())

a.seek(0)
a.seek(len(a.readlines()[0]))
print("\nme saltee la primera linea:\n", a.read())

a.seek(0)
""" lectura y escritura """
a.close()
a = open("archivo_txt", "r+")
a.write("ya no estudio python")
""" escribir tmb deja la barrita en el lugar """

a.seek(0)
print("\nescibiendo:\n", a.read())
""" la diferencia entre write y append es que append agrega texto al final y write sobreescribe
desde el principio. Si el texto nuevo es mas corto que el viejo no lo sobreescribe todo y se 
suma lo del anterior y es inentendible """

""" basicamente agarro todo y segunda linea la cambio y vuelvo a escribir todo
pero con el cambio """
a.seek(0)
txt_list = a.readlines()
txt_list[1] = "porque gracias a dios falto blanco"
a.seek(0)
a.writelines(txt_list)
print(txt_list)

a.close()
""" para que no entendi """

""" open solo crea el archivo si es para esccibir (w) """
b = open("writelines.txt", "w")
b = open("writelines.txt", "r+")
b.write("primera linea\nsegunda linea\ntercera linea")
b.seek(0)
""" GUARDA QUE HAY READLINE Y READLINESSSS """
b_list = b.readlines()
print(b_list)
b_list[1] = "segunda linea modificada"
print(b_list)
b.seek(0)
""" writelines es para escibir una lista pero no es que cada elemento tiene su linea. Eso depende
de si tienen el \n """
b.writelines(b_list)
b.close()
b = open("writelines.txt", "a")
b.seek(0)
b.write("agrego")
""" aunque ponga seek 0 agrega al final al ser append """
