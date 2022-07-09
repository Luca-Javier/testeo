""" Parece que no puedo solicitar atributos desde la clase. O sea que por eso necesitamos 
al constructor """


class coche():
    """ Metodo constructor. Al poner self.color es como crear y darle valor a una varaible color
    que se encuentra acá, en la clase """
    color = "azul"

    def __init__(self):
        """ Despues de experimentar lo del runi me doy cuenta de que le ponemos self para crearlaas
        tipo como estaban antes, en la clase. Por lo que me parece estupido poner los atributos acá.
        Los atributos que no solicite para crear mi objeto """
        self.color = "rojo"
        self.__ruedas = 4  # ahora ruedas es privada
        self.llendo = False
        #self.runi = ""
    """ Puedo comentar runi y despues con un self como que le creo el atributo en el momento
    pero como quiera hacer el print antes de declara runi. Error """

    def arrancar(self, arrancamos):
        self.llendo = arrancamos

    def estado(self):
        if self.llendo == True:
            run = "en marcha"
        else:
            run = "quieto"
        """ se puede usar la , para concatenar :O. Y encima deja un espacio"""
        try:
            print("El coche tiene", self.__ruedas,
                  "ruedas, es de color", self.color, "y está", run, self.runi)
        except AttributeError as runiNotDeclared:
            print("Usa antes el metodo 'setEstad'")

    def setEstad(self):
        if self.llendo == True:
            self.runi = "y corriendo"
        else:
            self.runi = "quietito"

    def createPrint(self):
        print(self.created)


car = coche()
car2 = coche()

car.arrancar(True)
car2.arrancar(False)

car.ruedas = 99  # aunque ponga los guiones o no. No va a cambiar.

car.setEstad()
""" car2.setEstad() """

car.created = "hola"  # creo created en la clase
car.createPrint()

car.estado()
car2.estado()
