""" es convertir un objeto o una lista a binario para poder guardarla y transportarla """
import pickle

name_list = ["Pedro", "Ana", "María", "Isabel"]
""" fichero es como un lugar donde guardar archivos """
fichero_binario = open("lista_nombres", "wb")  # wb = escritura binaria

pickle.dump(name_list, fichero_binario)

fichero_binario.close()

chek = open("lista_nombres", "rb")  # leer binario

print(pickle.load(chek))
