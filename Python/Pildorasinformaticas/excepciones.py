def sumar(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def divid(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se divide por 0")
        return "Imposible"


rta = ""
while rta != "sumar" and rta != "restar" and rta != "dividir":
    rta = input("Sumar, dividir o restar? ")

""" al pasar una letra el error está en la conversion a int """
""" pero como no se el error que es, lo hago con la division """
while True:
    try:
        num1 = int(input("Valor 1: "))
        num2 = int(input("Valor 2: "))
        break
    except ValueError:
        print("Inserte numero")

if rta == "sumar":
    print(f"La suma da {sumar(num1,num2)}")

elif rta == "restar":
    print(f"La resta da {resta(num1,num2)}")

elif rta == "dividir":
    print(f"La division da {divid(num1,num2)}")

else:
    print("Error")
""" yo si paso una letra da error y es obvio, pero el punto es que todo el programa se para.
Las excepsiones sirven para aunque salte error, el programa siga """

print("\n-----------------too errors-------------------")


def dividir():
    try:
        num1 = int(input("Valor 1: "))
        num2 = int(input("Valor 2: "))
        print("la division es: " + str(num1/num2))
        print("\nFIN")
    except ValueError:
        print("Inserte numeros")
        dividir()
    except ZeroDivisionError:
        print("No se divide por 0")
        dividir()


dividir()


def dividirr():
    try:
        num1 = int(input("Valor 1: "))
        num2 = int(input("Valor 2: "))
        print("la division es: " + str(num1/num2))
        print("\nFIN")
    except:
        print("ERROR")
        dividirr()
    finally:
        print("El sistema ha concluido")


""" el finally ejecuta pase lo que pase, aunque de error y no haya excepcion. En este caso da 
lo mismo pero bueno. Podria ser un finally close de DB o sockets """

dividirr()
