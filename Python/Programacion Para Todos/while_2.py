""" ciclos EJ: voy a un lugar y constantemente me pregunto "ya llegue". Si no llegue doy un
paso mas o sigo caminando, si ya llegue paso a hacer otra cosa 
un ciclo es una accion que se repite.
Hay 2 tipos de ciclos
  -mientras(while)
  -hasta(un rango, el for)"""
num = 0
while(True):
    # num++ #no existe esto acá
    num = num + 1
    print(num)
    if(num == 10):
        break

print("\n-----------Sumo los pares y multiplico los impares----------")
suma = 0
mult = 1

""" es curioso porque como el while y el programa sigue, estoy interactuando con el """
while num != 0:
    num = int(input("Dame un numero. Si me das un 0 termina: "))
    if num % 2 == 0:
        suma = num + suma
    else:
        mult = num * mult
    print(f"Suma: {suma}")
    print(f"Multiplicacion: {mult}\n")
print("finish")
