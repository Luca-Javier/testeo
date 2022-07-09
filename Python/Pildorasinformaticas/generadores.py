""" Una funcion """


def generarPares(cant):
    num = 1
    myList = []

    while num < cant:
        myList.append(num*2)
        print("h")
        num += 1
    return myList


print(generarPares(10))
print("")

""" así sería normal y ahora vamos a usar generadores """


def generarParess(cant):
    num = 1

    while num < cant:
        yield num*2
        print("h")
        """ yield va devolviendo mientras le llegan los valores, es un return constante """
        num += 1


print(generarParess(10))
devueltos = generarParess(10)
for i in devueltos:
    print(i)
print(devueltos)

print("----------EXPERIMENTO-----------------\n")


def generarParesss():
    while True:
        num = 1
        if input("otro?") == "otro":
            yield num*2
            num += 1
            break
        else:
            print("FIN")
            break


dev = generarParesss()

for i in dev:
    print(i)
""" FAIL. Creo que lo vamos a ver en otro video """
