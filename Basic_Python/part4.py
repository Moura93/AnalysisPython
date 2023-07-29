# CURSO COMPLETO DE PYTHON - PARTE 4
# YOUTUBE: PYTHONANADO
# LINK: https://www.youtube.com/watch?v=aJaTodJZIvM
# AUTOR: FELIPE

# FUNÇÕES #
import calculos


def EXIBE_BOM_DIA():
    print('Bom Dia!')
    print('Tudo bom?')


EXIBE_BOM_DIA()


def SOMA(n1, n2):
    RESULTADO = n1 + n2
    print(RESULTADO)


SOMA(5, 2)


def MEDIA(m1, m2):
    VALOR = (m1+m2)/2
    return VALOR


print(MEDIA(5, 9))

# IMPORT #
print(calculos.MODULO(5, 8))
