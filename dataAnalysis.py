import pandas as pd
import matplotlib.pyplot as plt
import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

dados = pd.read_excel(r"E:\MEGA\Documentos\Mestrado\Python\Base de dados\INMET\Patos\EC_PB_PATOS_2022.xlsx")

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)
print(dados.groupby('Data').mean())
# print(dados['Nebulosidade (Decimos)'].unique())
# fig = plt.figure()
# ax = fig.subplots()
# dados.groupby('Data').mean()['Vel. Vento (m/s)'].plot(kind='hist')
# plt.grid()
# plt.show()


