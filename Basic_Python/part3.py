# CURSO COMPLETO DE PYTHON - PARTE 3
# YOUTUBE: PYTHONANADO
# LINK: https://www.youtube.com/watch?v=aJaTodJZIvM
# TUPLAS: https://www.youtube.com/watch?v=6PACWNWEaJ8
# AUTOR: FELIPE

# ESTRUTURA DE DADOS #
# LISTAS #
IDADES = [21, 22, 18, 35]
print(IDADES)
IDADES.pop(1)  # REMOVE O VALOR DO LOCAL 1
print(IDADES)
IDADES.append(100)
print(IDADES)

NOTAS = []
while True:
    NOTA = int(input('Digite uma nota ou -1 para sair: '))
    if NOTA == -1:
        break
    NOTAS.append(NOTA)
for i in NOTAS:  # Esse for percorre toda a lista e atribui um valor da lista a i
    print(i)
SOMA = 0
for i in NOTAS:
    SOMA = SOMA + i
print(f"A soma das notas é: {SOMA}")
MEDIA = SOMA/len(NOTAS)  # o len retorna a quatidade de itens da lista
print(f"A média das notas é: {MEDIA}")

# TUPLAS #
tupla = (1, 3, 8, 'Daniel')
print(f"O valor item da Tupla é: {tupla[0]}")
tupla = (5, 3, 8, 'Daniel')
print(f"O valor item da Tupla é: {tupla[0]}")

# DICIONÁRIOS #
PESSOA = {'nome': 'Caio Sampaio', 'idade': 22, 'cidade': 'Franca'}
print(PESSOA)
print(PESSOA['nome'])
LISTA_DE_DICIONARIOS = [{'nome': 'Caio Sampaio', 'idade': 22, 'cidade': 'Rio de Janeiro'}, 
                        {'nome': 'João Pedro', 'idade': 18, 'cidade': 'Recife'},
                        {'nome': 'Pedro Albuquerque', 'idade': 32, 'cidade': 'Natal'},
                        {'nome': 'Fernando Pessoa', 'idade': 50, 'cidade': 'Brasilia'}
                        ]
print(LISTA_DE_DICIONARIOS[1]) # Printa o item da posição 1 da lista, que é um dicionário
print(LISTA_DE_DICIONARIOS[2]['nome']) # Printa o item nome da posição 2 da lista