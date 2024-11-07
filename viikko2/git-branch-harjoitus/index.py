#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")# muutos main-haarassa

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") # muokattu mainissa
print(f"{x} - {y} = {erotus(x, y)}") # muokattu mainissa

logger("lopetetaan ohjelma")
print("Moikka!")#lisäys bugikorjaus-branchissa