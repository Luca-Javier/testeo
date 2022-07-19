import pickle

""" si abro con write se borra todo lo que estaba en el archivo """
a = open("test", "a+")
print(a.read())
a.close()
""" MI TEORÍA: append abre el archivo y deja el puntero al final, para agregar. """
