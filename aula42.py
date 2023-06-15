frase = 'atilla'
qnt_etra_apareceu_mais = 0
i = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):  
    letra_atual = frase[i]
    quantas_vezes_letra_apar = frase.count(letra_atual)
    i+=1
    if letra_atual == ' ':
        continue

    
    if qnt_letra_apareceu_mais < quantas_vezes_letra_apar:
        qnt_letra_apareceu_mais = quantas_vezes_letra_apar
        letra_apareceu_mais_vezes = letra_atual
print('A letra que apareceu mais vezes foi'f'"{letra_apareceu_mais_vezes}" que apareceu {qnt_letra_apareceu_mais} vezes')
    

    
    
    