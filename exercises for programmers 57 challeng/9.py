import math

length = float(input("what is the length of the room in feet? "))
width = float(input("what is the width of the room in feet? "))

squarefeet = length * width

tinta = math.ceil(squarefeet / 360)

print('you will need to purchase', tinta)