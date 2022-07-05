from itertools import count


txt = input("Ingresa un texto para que yo lo analize: ")
""" l = letra """
l1 = input("dame una letra: ")
l2 = input("dame otra letra: ")
l3 = input("dame otra letra: ")

l1_cant = txt.upper().count(l1.upper())
l2_cant = txt.upper().count(l2.upper())
l3_cant = txt.upper().count(l3.upper())

txt_list = txt.split()
print(txt_list)
palabras_cant = len(txt_list)

# z = txt_list.reverse() #no devuelve nada
""" DESCUBRÍ que si mantengo el click en reverse() me dice si devuelve o no
Sale -> none. Si sale otra cosa no es none """
txt_list.reverse()
e = " ".join(txt_list)

dic = {'False': 'No, no está', 'True': 'Si, si está'}
""" También pude """
dicxd = {False: 'No, no está', True: 'Si, si está'}
print(
    f"\nDentro del texto que me mandaste hay {l1_cant} {l1}, {l2_cant} {l2} y {l3_cant} {l3}")
print(f"Hay {palabras_cant} palabras")
print(f"La primera letra es {txt[0]} y la ultima es {txt[-1]}")
print(f"""El texto al revez es así:
{e}""")
print(
    f"La palabra Python esta en el texto?. {dic[str('python' in txt.lower())]}")
