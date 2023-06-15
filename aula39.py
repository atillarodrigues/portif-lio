#calculadora com while
while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador que você deseja usar "+(soma), -(subtração), /(divisão), *(multiplicação): "')
    numeros_validos =  None
    num_1_flot = 0
    num_2_flot = 0
    operadores_permitidos = 0
    

    try:
        num_1_flot = float(numero_1)
        num_2_flot = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('O operador digitado é invalido!')
        continue
    if len(operador) >1 :
        print('Digite apenas um operador!')
        continue
    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_flot} + {num_2_flot}=',num_1_flot + num_2_flot)
    elif operador == '-':
        print(f'{num_1_flot} - {num_2_flot}=',num_1_flot - num_2_flot)
    elif operador == '*':
        print(f'{num_1_flot} * {num_2_flot}=',num_1_flot * num_2_flot)
    elif operador == '/':
        print(f'{num_1_flot} / {num_2_flot}=',num_1_flot / num_2_flot)
    else:
        print('Critical error!')
    
    sair = input('Que sair? [s]im [n]ão: ').lower().startswith('s')
    if sair is True:
        print('Programa encerrado. Obrigado por usar o programa')
        break
    if sair is False:
        continue
