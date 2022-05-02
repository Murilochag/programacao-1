import math



def logba2(x):
    x = (math.log(x,10))
    return x

def cartao(apr, b, p) :
    i = apr / 36500
    a = -(1 / 30)
    c = (1 + (b / p) * (1 -((1 + i)**30)))
    d = logba2(c)
    e = logba2(1 + i)

    n = a * (d / e)
    return n

print(math.ceil(cartao(12,5000,100)))