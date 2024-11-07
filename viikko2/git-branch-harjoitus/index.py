#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")# muutos main-haarassa

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")# muokattu bugikorjaus-branchissa
print(f"{x} - {y} = {erotus(x, y)}") # muokattu mainissa

logger("lopetetaan ohjelma")
print("Moikka!")#lisäys bugikorjaus-branchissa