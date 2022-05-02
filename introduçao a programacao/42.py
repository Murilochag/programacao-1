import math

angulo = float(input("\nentre com um angulo em graus: "))
rang = angulo * math.pi / 180

print("\nseno:",math.sin(rang),"\ncoseno:",math.cos(rang),"\ntangente:",math.tan(rang),"\ncosecante:",(1 / math.sin(rang)),"\nsecante:",(1 / math.cos(rang)),"\ncotangente:",(1 / math.tan(rang)),"\n")