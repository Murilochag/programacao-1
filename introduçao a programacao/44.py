from cmath import log
import math


numero = float(input("entre com um logaritmando: "))
base = float(input("entre com a base; "))
logaritmo = math.log(numero) / math.log(base)
print("\no logaritmo de",numero,"na base",base,"é",logaritmo)
