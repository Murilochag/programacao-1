a = float(input('total alcohol consumed: '))
w = float(input('body weighi in pounds: '))
g = input('what is your gener?(w/m): ')
h = float(input('number of hours: '))

if g == 'M' or 'm' :
    r = 0.73
elif g == 'W' or 'm' :
    r = 0.66
else: r = 3550

if r == 0.66 or 0.73 :
    bac = (a * 5.14 / w * r) - 0.15 * h

    print('your BAc is', bac)

    if bac <= 0.08 : print('it is legal for your to drive!')
    else: print('it is not legal for your to drive!')
else: print('erro!')    
