print("Vamos a calcular un promedio")
cant = int(input("Cuantos numero me vas a dar: "))
suma = 0

""" No entiendo que es range(). No lo puedo printear, verl el type """
for valor in range(cant):
    nums = int(input(f"Ingrese el numero {valor+1}: "))
    suma += nums
promedio = suma / cant
print(f"El promedio es {promedio}")
