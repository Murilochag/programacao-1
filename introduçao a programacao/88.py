print('***************\nCALCULADORA\n***************')
print('\n\nsomar: + \nsubtrair: - \nmultiplicar: * \ndividir: /')

resp = input('digite uma opção: ')

if resp == '+' :
    a = float(input('entre com um número: '))
    b = float(input('entre com outro número: '))
    print('a soma entre',a, 'e',b, 'é' ,(a + b))
elif resp == '-' :
    a = float(input('entre com um número: '))
    b = float(input('entre com outro número: '))
    print('a subtração entre',a, 'e',b, 'é' ,(a - b))
elif resp == '*' :
    a = float(input('entre com um número: '))
    b = float(input('entre com outro número: '))
    print('a multiplicação entre',a, 'e',b, 'é' ,(a * b))
elif resp == '/' :
    a = float(input('entre com um número: '))
    b = float(input('entre com outro número: '))
    print('a divisão entre',a, 'e',b, 'é' ,(a / b))
else: print('desculpe, opção não disponível :(')