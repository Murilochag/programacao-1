import math

raio = float(input("raio: "))

tetoRedondo = math.pi * (raio * raio)

tinta = math.ceil(tetoRedondo / 360)

print('you will need to purchase', tinta, "gallons of")