# PYTHON - ORIENTAÇÃO A OBJETO
# LINK (HASHTAG) = https://www.youtube.com/watch?v=yGaVJZuSr9I
# LINK (HASHTAG) = https://www.youtube.com/watch?v=97A_Cyyh-eU
# LINK (HASHTAG) = https://www.youtube.com/watch?v=gomDSZaay3E
# AUTOR: FELIPE

# CLASSES
#     -> ATRIBUTOS
#     -> METODOS

# class classe():
#     atributo
#     metodo
# OBJETO

# INSTÂNCIA

class Vendedor():  # Toda classe inicia com letra maiuscula
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas): #METODO
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f"O vendedor {self.nome} bateu a meta")
        else:
            print(f"O vendedor {self.nome} não bateu a meta")


vendedor1 = Vendedor("Felipe")
vendedor1.vendeu(1000)  # Atribução do valor de vendas
vendedor1.bateu_meta(600)  # Atribuição da meta e Verificação se ele bateu a meta
