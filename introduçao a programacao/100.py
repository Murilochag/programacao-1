num = float(input('entre com um número de 4 algorismos: '))
c = num % 100

if (c % 4) == 0 :
    print('\n',num,'é multiplo de 4 \n')
else : print('\n',num,'não é multiplo de 4 \n')