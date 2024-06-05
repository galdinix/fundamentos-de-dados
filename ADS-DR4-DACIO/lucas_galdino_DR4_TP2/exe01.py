#Desenvolva um programa que, dado uma lista de nomes com possíveis duplicatas, 
#retorne um dicionário contendo a contagem de cada nome. 
#Além disso, ele deve remover qualquer nome que apareça apenas uma vez, 
#utilizando técnicas de manipulação de dicionários.

nomes = ['lucas', 'lucas', 'nay', 'nay', 'nay', 'gui', 'dacio']
dict_nome = {}

for nome in nomes:
    if nome in dict_nome:
        dict_nome[nome] += 1
        continue
    dict_nome[nome] = 1
    
dict_nome_atualizado = {chave: valor for chave, valor in dict_nome.items() if valor > 1}    
print(f'Contagem de nomes retirando os que possuem uma aprição:\n{dict_nome_atualizado}')