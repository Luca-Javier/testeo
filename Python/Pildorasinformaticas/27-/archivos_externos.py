from io import open

""" primero le pasamos el nombre del archivo y segundo le pasamos el modo, como vamos a usar 
el archivo o para que. Los modos son: lectura, escritura, append (agregar informacion a una 
archivo que ya tiene informacion)"""
archivo_txt = open("archivo_txt", "w")
""" si ejecutamos el codigo y el archivo no existe, crea uno """
frase = "estudiando python \nun viernes \nporque falto blanco"
archivo_txt.write(frase)
archivo_txt.close()

read_archivo = open("archivo_txt", "r")
print(read_archivo.read())
read_archivo.close()

""" trae una lista y almacena lineas """
read_lines = open("archivo_txt", "r")
print("\nLineas:\n" + str(read_lines.readlines()[0]))
read_lines.close()

agregar = open("archivo_txt", "a")  # ?append

agregar.write("\nagregando info")
agregar.close()

""" es lo mismo """
agregar2 = open("append_vacio", "a")
agregar2.write("agrego info donde no habia nada. O sea escibo")
agregar2.close()
