a = float(input('lado A: '))
b = float(input('lado B: '))
c = float(input('lado C: '))

if a < b + c and b < a + c and c < a + b :
    if a == b and a == c :
        print('\nTriangulo equilátero\n')
    elif a == b or a == c or b == c :
        print('\nTriângulo isósceles\n')
    else : print('\nTriângulo escaleno\n')