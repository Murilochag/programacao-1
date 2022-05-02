a = float(input('lado A: '))
b = float(input('lado B: '))
c = float(input('lado C: '))

if a < b + c and b < a + c and c < a + b :
    if a > b and a > c :
        maior = a ** 2
        lados = b ** 2 + c ** 2
    elif b > c :
        maior = b ** 2
        lados = a ** 2 + c ** 2
    else : 
        maior = c ** 2
        lados = a ** 2 + b ** 2


    if maior == lados :
        print('\nTriãngulo  retângulo\n')
    elif maior > lados :
        print('\nTriãngulo obtusângulo\n')
    else : print('\nTriângulo acutângulo\n')
else : print('\nas medidas não formão um triângulo\n')