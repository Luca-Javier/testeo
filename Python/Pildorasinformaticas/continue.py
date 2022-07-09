from operator import truediv
from pickle import FALSE, TRUE


nombre = "Juan Carlos"
print(f"el nombre mide {len(nombre)}")

cant = 0
for letras in nombre:
    """ skipeo el vacio y tengo la cantidad de letas, no la longitud de la cadena """
    if letras == " ":
        continue
    cant += 1

print("Pero tiene " + str(cant) + " letras")

arroba = False
mail = input("\nIntroduce tu email: ")
for i in mail:
    if i == "@":
        arroba = True
        break
"""   else:
    arroba = False """
if arroba == True:
    print("correcto")
else:
    print("no es un email valido")


class obj:
    pass


""" pass es null, es como no hacer nada. Si quiero crear mi clase pero no trabajarla ahora puedo
crearla, ponerle el pass y seguir con otra cosa. Tambien podria comentarla eh, pero bueno, con
el pass destacara mas """

print("pass")
