from pickle import FALSE

""" https://www.youtube.com/watch?v=Y_SiIgxc-xI&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=26&ab_channel=pildorasinformaticas """


class coche():
    color = "rojo"
    ruedas = 4
    llendo = False

    def arrancar(self):
        self.llendo = True

    def arrancarr(c):
        c.llendo = True

    def conPass():
        pass

    def estado(self):
        if self.llendo == True:
            return "El coche está en marcha"
        else:
            return "El no coche está en marcha"
    # def sinPass(): #da error porque termna agarrando a car y piensa que no esta tabulado


car = coche()  # no usamos new

print(f"El color de mi coche es {car.color}")
print(f"Mi coche tiene {car.ruedas} ruedas")
# car.conPass()  # no pasa nada, no da error
""" CORRECION: si da error si tenog mas codigo abajo. Concluyo con que el pass es solo para que
no pase lo del "sinPass" """
car.arrancar()


""" Explicacion Self: el self es el this y lo que pasa es que en java y otro lenguajes, pero 
yo solo conozco java, el this está implicito. El this significa "mio". Y de quien es?. De 
mi objeto.
Mi objeto coche tiene atributos, en este caso no solicito atributos para la constuccion del mismo
, pero si lo hiciera, cada coche puede tener diferente atributos. Cuestion que el self se 
refiere al atributo de mi objeto"""
car.arrancarr()
""" al crea un metodo no tenemos que enviar car.arrancarr(car). Por que el enviar nuestro
objeto es implicito. Pero python si quiere que el primer valor que reciba la funcion sea el
objeto. Como vemos no hace falta que se llame self"""

""" Conclusión: el this que nunca entendí, no se refiere a estos datos, de esta clase. Se 
refiere a estos datos de este objeto que esta ejecutando la funcion. Solo que en python es 
explicito la solicitud del objeto """

print(car.estado())
car2 = coche()
print(car2.estado())
""" solo es true el valor del coche 1, su propio valor, su self.llendo. Pero no el del coche2 """
