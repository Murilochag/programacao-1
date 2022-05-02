numero = float(input('entre com um número: '))

if (numero % 10 ) == 0 :
    print(numero,'é multiplo de 10')
elif(numero % 2) == 0 :
    print(numero,'é multiplo de 2')
elif(numero % 5) == 0 :
    print(numero,'é multiplo de 5')
else : print('não é multiplo de 10, 2 nem 5')