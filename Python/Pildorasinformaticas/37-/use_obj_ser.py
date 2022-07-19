import pickle

chek = open("cochesGuardados", "rb")
loadCoches = pickle.load(chek)
chek.close()
del chek

for c in loadCoches:
    print(c)
""" en la serializacion guardo la info de mi objeto pero no la clase y sus metodos. Es como que
guardo que tengo un objeto vehiculo pero no se que es un objeto vehiculo porque no existe """
