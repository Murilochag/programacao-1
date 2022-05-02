a = float(input('lado A: '))
b = float(input('lado B: '))
c = float(input('lado C: '))

if a < b + c and b < a + c and c < a + b :
    print('\npodem ser lados de um triângulo\n')
else:print('\nnao podem ser lados de um triângulo\n')