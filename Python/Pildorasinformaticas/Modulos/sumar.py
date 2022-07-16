""" 
def sumar(*num):
    suma = 0
    p1 = 0
    p2 = 1
    while True:
        if num[p2]:
            rta = num[p1] + num[p2]
            suma += rta
            p1 += 2
            p2 += 2
        else:
            if num[p1]:
                suma += num[p1]
            else:
                break
    print("El resultado de la suma es:", suma)
"""

""" xd """


def sumar(*num):
    suma = 0
    for h in num:
        suma += h
    print("El resultado de la suma es:", suma)


""" def sumar(num1, num2):
    print("El resultado de la suma es:", num1 + num2) """


def restar(num1, num2):
    print("El resultado de la resta es:", num1 - num2)


def multiplicar(num1, num2):
    print("El resultado de la multiplicacion es:", num1 * num2)
