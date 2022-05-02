#-------------------------------------------------

#--------------  Algoritmo 23  --------------------

#-------------------------------------------------

a = int(input("digite um número de tres casas: "))
d = a % 100
d = int(d / 10)
print("algorismo da casa das dezenas:", d)

#-------------------------------------------------

#--------------  Algoritmo 25  --------------------

#-------------------------------------------------

data = int(input("escreva uma data: "))
dia = int(data / 10000)
mes = int((data % 10000) / 100)
ano = int(data % 100)
print("dia:",dia,"\nmês",mes,"\nano:",ano)

#-------------------------------------------------

#--------------  Algoritmo 34  --------------------

#-------------------------------------------------

numero = int((input("entre com um número inteiro: ")))
ant = numero - 1
suc = numero + 1
print("o sucessor de",numero,"é",suc,"e o antecessor é",ant)

#-------------------------------------------------

#--------------  Algoritmo 38  --------------------

#-------------------------------------------------

num = float(input("entre com um número real: "))
num /= 3
print("a terca parte é",num)

#-------------------------------------------------

#--------------  Algoritmo 39  --------------------

#-------------------------------------------------

nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
media = (nota1 + nota2) / 2
print("média:",media)

#-------------------------------------------------

#--------------  Algoritmo 40  --------------------

#-------------------------------------------------

num1 = int(input("entre com o dividendo: "))
num2 = int(input("entre com o divisor: "))

quociente = num1 / num2
resto = num1 % num2

print("\ndividendo:",num1,"\ndivisor:",num2,"\nquociente:",quociente,"\nresto:",resto,"\n")

#-------------------------------------------------

#--------------  Algoritmo 41  --------------------

#-------------------------------------------------

a = float(input("entre com número 1: "))
b = float(input("entre com número 2: "))
c = float(input("entre com número 3: "))
d = float(input("entre com número 4: "))

mp = (a*1 + b*2 + c*3 + d*4) / 10

print("média ponderada:",mp)

#-------------------------------------------------

#--------------  Algoritmo 42  --------------------

#-------------------------------------------------

import math

angulo = float(input("\nentre com um angulo em graus: "))
rang = angulo * math.pi / 180

print("\nseno:",math.sin(rang),"\ncoseno:",math.cos(rang),"\ntangente:",math.tan(rang),"\ncosecante:",(1 / math.sin(rang)),"\nsecante:",(1 / math.cos(rang)),"\ncotangente:",(1 / math.tan(rang)),"\n")

#-------------------------------------------------

#--------------  Algoritmo 43  --------------------

#-------------------------------------------------

import math

numero = float(input("entre com o logaritmando: "))
print("\nlogaritmo: ",math.log10(numero),"\n")

#-------------------------------------------------

#--------------  Algoritmo 44  --------------------

#-------------------------------------------------

from cmath import log
import math


numero = float(input("entre com um logaritmando: "))
base = float(input("entre com a base; "))
logaritmo = math.log(numero) / math.log(base)
print("\no logaritmo de",numero,"na base",base,"é",logaritmo)
