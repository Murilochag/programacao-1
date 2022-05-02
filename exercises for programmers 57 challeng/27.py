def isNotVazia(entrada):
    return entrada != ''

def atlext2(entrtada):
    return len(entrtada) >= 2

def isNumber(entrada):
    return entrada.isnumeric()

def isValidID(entrada):
    parts = entrada.split('-')
    if len(parts) != 2:
        return False
    return isletter(parts[0]) and isNumber(parts[1])

nome = input('nome:')
sobrenome = input('sobrenome:')
idfunci = input('ID:')
