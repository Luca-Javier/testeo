import os
import random

adivinar = random.randint(1, 10)
user = -1

""" while user != adivinar:
    os.system('cls')
    user = int(input("Cual es el numero?: "))
    if user < adivinar:
        print("más grande")
    if user > adivinar:
        print("más chico")
    input("Enter para continuar")

print("\nFIN") """

machine = -1

while user != adivinar and machine != adivinar:
    os.system('cls')
    user = int(input("Numero ha adivinar: "))
    if user < adivinar:
        print("más grande")
    elif user > adivinar:
        print("más chico")
    else:
        print("Usuario gana")
        break
    input("Enter para continuar")
    print("\nMaquina:")
    machine = random.randint(1, 10)
    print(machine)
    if machine < adivinar:
        print("más grande")
    elif machine > adivinar:
        print("más chico")
    else:
        print("Maquina gana")
        break
    input("Enter para continuar")

print("\nFIN")
