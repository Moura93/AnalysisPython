import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\fmour\Documents\MEGAsync Downloads\Documentos\Mestrado\Python\Base de dados\Kaggle\50Hertz.xlsx")

pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 180)
pd.set_option('display.max_colwidth', None)

# mensal = df.groupby(['MÊS']).mean()
mensal = df.loc[:, datetime.time(00,00,00):datetime.time(23,45,00)]
mensal = mensal.mean(axis=1)


print(mensal)
# mensal.catplot(data=mensal, x="MÊS")

# plt.plot(mensal)
# plt.show()