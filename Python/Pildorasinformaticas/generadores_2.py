""" si ponemos *ciudades le decimos, o que no sabemos cuantos parametros les vamos a pasar, o
que les vamos a pasar infinito o es random. Tambien significa que los valores que le pasemos 
van a estar en una tupla """


def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento


ciudades = devuelveCiudades("Madrid", "Barcelona",
                            "Bilbao", "Valencia", "Buenos aires", "Marico")

for i in ciudades:
    print(i)


""" next() imprime el siguiente en un array iterativo """
c = 0
lisa = iter([1, 2, 3, 4, 5, 6])
while c != 3:
    c = int(next(lisa))
    print(c)

print("Yield from:\n")


def devuelveCiudadess(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
        # yield subElemento
        yield from elemento
        """ parece tipo un for in pero generador """


dev = devuelveCiudadess("Madrid", "Barcelona",
                        "Bilbao", "Valencia", "Buenos aires", "Marico")
print(next(dev))
print(next(dev))
print(next(dev))
