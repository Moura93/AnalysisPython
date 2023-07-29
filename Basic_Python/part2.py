# CURSO COMPLETO DE PYTHON - PARTE 2
# YOUTUBE: PYTHONANADO
# LINK: https://www.youtube.com/watch?v=aJaTodJZIvM
# AUTOR: FELIPE

# ESTRUTURA DE CONDIÇÕES #
k = True
if k:
    print('Fui executado')

NOTA1 = int(input('Digite a 1º nota: '))
NOTA2 = int(input('Digite a 2º nota: '))
MEDIA = (NOTA1+NOTA2)/2

if MEDIA >= 7:
    print(f"Aluno com média {MEDIA} Aprovado!")
elif MEDIA >= 4 and MEDIA < 7:
    print(f"Aluno com média {MEDIA} Recuperação")
else:
    print(f"Aluno com média {MEDIA} Reprovado")

# ESTRUTURAS DE REPETIÇÃO #
n = 1
i = 1
# WHILE #
while n <= 11:
    if n == 6:
        break
    print(f"Iteração: {n}")
    n += 1
while i <= 5:
    print(f"Interação2: {i}")
    i += 1
# FOR #
# range(x, y) -> x é o valor inicial e y é o valor que ele para o loop (ele não loopa no valor final)
# range(x, y, z) -> z é a quantidade que ele vai somando no loop
for j in range(5, 15, 2):
    print(j)
for x in range (1, 11):
    for y in range(1, 11):
        print(f"{x} x {y} = {x*y}")
