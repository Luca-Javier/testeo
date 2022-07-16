#nombre = input("Ingrese nombre: ")
nombre = "roBerTo"

print(f"EL nombre es {nombre}")
print(f"EL nombre es {nombre.lower()} (todo minuscula)")
print(f"EL nombre es {nombre.upper()} (todo mayuscula)")
print(f"EL nombre es {nombre.capitalize()} (Primera mayuscula)")

edad = "35"
edad = "35 años"
print(f"La edad es {edad} y ¿Es un digito?: {edad.isdigit()}")

print("\n------------------Ejercicio--------------------\n")

mail = input("Cual es tu gmail? ")

position = mail.find("@")
# print(len(mail))
if position == 0 or position == len(mail)-1 or position == 0 - 1:
    print("Inserte un gmail verdadero")
else:
    print("Correcto")
