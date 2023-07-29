# CURSO COMPLETO DE PYTHON - PARTE 1
# YOUTUBE: PYTHONANADO
# LINK: https://www.youtube.com/watch?v=aJaTodJZIvM
# AUTOR: FELIPE

# ENTRADA DE DADOS #
NOME = input('Qual seu nome? ')

print(f"Seu nome é? {NOME}")
print(f"O tipo da variável é: {type(NOME)}")

# CONVERSÃO DE DADOS #
NOTA1 = int(input('Digite a primeira nota: '))
NOTA2 = int(input('Digite a segunda nota: '))
MEDIA = (NOTA1+NOTA2)/2
print(f"Sua primeira nota foi: {NOTA1}\nSua segunda nota foi: {NOTA2}\nSua média foi: {MEDIA}")

# OPERADORES ARITIMÉTICOS #
# + SOMA
# - SUBTRAÇÃO
# / DIVISÃO
# * MULTIPLICAÇÃO
# ** EXPONENCIAÇÃO
# // DIVISÃO SEM RESTO
# % RESTO DA DIVISÃO

# OPERADORES RELACIONAIS #
# <     # ==    # <=
# >     # !=    # >=
operador_relacional = 5 > 6
print(operador_relacional)

# OPERADORES LÓGICOS #
# and
# or
# not
operador_logico = True and False
print(operador_logico)
operador_logico = True or not False
print(operador_logico)
    