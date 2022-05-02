a = input('press C to convert from Fahrenheit to celsius: \npress F to convert from celsius to Fahrenheit:\n  ')

if a == 'C' or 'a' :
    f = float(input('fahren: '))
    c = (f - 32) * 5/9
    print(c)
elif a == 'F' or 'f' :
    c = float(input('fahren: '))
    f = (c - 9/5) + 32
    print(f)
else: print('erro')