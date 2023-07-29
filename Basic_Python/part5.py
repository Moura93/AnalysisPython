# COMPLEMENTO DO CURSO DE PYTHON
# w3school: Sets / Dir / Lambda / Map
# LINK (LAMBDA) = https://www.youtube.com/watch?v=xmMXULd0dxc
# LINK (MAP) = https://www.youtube.com/watch?v=GEciIuxcWkg
# AUTOR: FELIPE

# SETS #
# SÃO LISTAS DESORDENADAS E IMUTÁVEIS, PORÉM VOCÊ PODE ADICIONAR E EXCLUIR ITENS
myset = {"feijão", "arroz", "banana", 2, 4}
print(myset)
print(len(myset))  # TAMANHO DO SET
myset.add(3)  # ADICIONA O ITEM
myset.discard(4)  # REMOVE O ITEM
print(myset)

# DIR #
# dir() mostra os comenados que podem ser usados (o que as funções podem fazer)
print(dir(set))

# LAMBDA #
# É uma pequena função anônima
def ISS(preco): return preco * 0.11
def MEDIA(a, b): return (a+b)/2

print(ISS(100))
print(f"A média é: {MEDIA(5, 9)}")

# MAP #
# é uma função que faz o cálculo de uma função com vários valores de uma vez
VALORES = [55, 60, 80, 150, 380]
# ou IMPOSTOS = list(map(lambda preco : preco * 0.11 , VALORES))
IMPOSTOS = list(map(ISS, VALORES))
print(f'Os valores de imposto de ISS foram: {IMPOSTOS}')
NOTAS1 = [5.4, 6.1, 8, 7.5, 2, 9]
NOTAS2 = [9, 7, 6.8, 8, 5.9, 6.5]
MEDIAS = list(map(MEDIA, NOTAS1, NOTAS2))
print(f'As médias dos alunos foram: {MEDIAS}')
