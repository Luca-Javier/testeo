""" modulos son otros archivos para despues importar y no repetir codigo. Un archivo modulo
puede tener extension py, pyc, c  """

""" Para importar desde una carpeta, en verdad es complicado, asi que usamos una libreria """


""" import sys
sys.path.append("/Modulos") """
# ? esta libreria es para importar de directorios re lejos

""" en conclusion el from se encarga de llegar al archivo y el import se fija que tiene que traer de el"""
import vehiculos
import sumar as mat
from sumar import restar
from sumar import *  # importo los metodos tal cual, como si los hubiera escrito acá
mat.sumar(5, 5, 8)
mat.restar(10, 5)

restar(10, 5)

multiplicar(2, 4)

miVehiculo = vehiculos.vehiculo("Honda", "C300")
miVehiculo.estado()
