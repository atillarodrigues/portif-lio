
import re
import sys

cpf_enviado_usuario = re.sub(r'[^0-9]','',input('Digite um CPF: '))
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo1 = 10
resultado_digito1 = 0
dez_digitos = cpf_enviado_usuario[:10]
contador_regressivo2 = 11
resultado_digito2 = 0
entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador_regressivo1
    contador_regressivo1 -=1
digito_1 = (resultado_digito1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0
# print(digito_1)

for digito in dez_digitos:
    resultado_digito2 += int(digito) * contador_regressivo2
    contador_regressivo2 -=1
digito_2 = (resultado_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0
# print(digito_2)
cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_calculado == cpf_enviado_usuario:
    print('O CPF DIGITADO É VALIDO')
else:
    print('CPF inválido, tente novamente')
    