def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total)
    return total

mult(2, 3, 4)

def par(numero):
    resto = 0
    resto = numero % 2
    if resto == 0:
        print(f'O numero: {numero} é par')
        return 'par'
    print(f'O numero: {numero} é impar')
    return 'impar'
            

par(2)

