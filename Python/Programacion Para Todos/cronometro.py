import os
import time
import os

""" hora = 0
minutos = 0
segundos = 0
 """
""" while hora != 1: """
for hora in range(2):
    for minutos in range(10):
        for segundos in range(10):
            os.system('cls')
            print(f"{hora}:{minutos}:{segundos}")
            time.sleep(.000000001)
print("Otro dia")
