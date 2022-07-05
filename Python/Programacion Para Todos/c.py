from ast import While
import os

user = 'pepe'
contra = 'vidrio'

""" python no tiene constantes, pero al declarar una variable con mayusculas entendemos que 
estamos hablando de una constante. Es una regla universal de la comunidad de python """
USER = ''
PASSWORD = ''

""" DUDA: como cambio una constante?. O sea si la declaro de nuevo obvio que la cambio, pero 
como tengo que cambiarla para poner a prueba su caracteristica """
while USER != user or PASSWORD != contra:
    """ para limpiar la terminal """
    os.system('cls')
    print("Intente de nuevo")
    USER = input("Usuario: ")
    PASSWORD = input("Contraseña: ")
""" en este caso modifique una constante. Pero no se si es porque en python no hay constantes
o porque las constantes son informales, en general """
print("Ha ingresado")
