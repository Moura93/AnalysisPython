import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_excel(r'Velocidades_1994-2003.xlsx')
df['Vel'] = np.sqrt((df['u']**2)+(df['v']**2))

hp = 1

# Hodrick-Prescott Filter
paracuru_cycle_1000, paracuru_trend_1000 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==1000], lamb=hp)
# paracuru_cycle_975, paracuru_trend_975 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==975], lamb=hp)
# paracuru_cycle_950, paracuru_trend_950 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==950], lamb=hp)
# paracuru_cycle_925, paracuru_trend_925 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==925], lamb=hp)
# paracuru_cycle_900, paracuru_trend_900 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==900], lamb=hp)
# paracuru_cycle_875, paracuru_trend_875 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==875], lamb=hp)
# paracuru_cycle_850, paracuru_trend_850 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==850], lamb=hp)
# paracuru_cycle_825, paracuru_trend_825 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==825], lamb=hp)
# paracuru_cycle_800, paracuru_trend_800 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==800], lamb=hp)
# paracuru_cycle_775, paracuru_trend_775 = sm.tsa.filters.hpfilter(df['Vel'].loc[df['level']==775], lamb=hp)

# plt.subplot(5,2,1)
plt.plot(paracuru_trend_1000)
plt.title("Pressão de Nível 1000")
# plt.subplot(5,2,2)
# plt.plot(paracuru_trend_975)
# plt.title("Pressão de Nível 975")
# plt.subplot(5,2,3)
# plt.plot(paracuru_trend_950)
# plt.title("Pressão de Nível 950")
# plt.subplot(5,2,4)
# plt.plot(paracuru_trend_925)
# plt.title("Pressão de Nível 925")
# plt.subplot(5,2,5)
# plt.plot(paracuru_trend_900)
# plt.title("Pressão de Nível 900")
# plt.subplot(5,2,6)
# plt.plot(paracuru_trend_875)
# plt.title("Pressão de Nível 875")
# plt.subplot(5,2,7)
# plt.plot(paracuru_trend_875)
# plt.title("Pressão de Nível 850")
# plt.subplot(5,2,8)
# plt.plot(paracuru_trend_875)
# plt.title("Pressão de Nível 825")
# plt.subplot(5,2,9)
# plt.plot(paracuru_trend_875)
# plt.title("Pressão de Nível 800")
# plt.subplot(5,2,10)
# plt.plot(paracuru_trend_875)
# plt.title("Pressão de Nível 775")



plt.show()
print(df)
