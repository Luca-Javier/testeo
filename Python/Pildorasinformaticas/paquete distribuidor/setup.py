from setuptools import setup
""" el archivo tiene que llamarse setup.py si o si """
setup(
    name="paquete",
    author="Luca-Javier",
    author_email="luca.jav45@gmail.com",
    description="es un paquete que...",
    version="1.0",
    url="www.javier.com",
    packages=["paquete_distribuido", "paquete_distribuido"],
    scripts=[]
)
""" packages es el mas importante. Ahí ponemos lo que vamos a distribuir y despues la direccion """

""" una vez creado todo esto tenemos que con powershell o cmd entrar en esta ubicación (con 
shift y click derecho tenemos la opcion de abrir shell donde estamos) y ejecutar el comando:
python "nombre archivo" sdist

esto nos va a generar una carptea dist y dentro un rar y este es el paquete que tenemos que
distribuir. Otra ve vamos la direccion de este rar y ejecutamos 
pip3 install "nombre archivo" """
""" llamo los archivos en con al archivo usando_dist.py """
