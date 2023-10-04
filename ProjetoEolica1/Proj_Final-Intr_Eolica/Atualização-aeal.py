import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
import pandas as pd
import math

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv(r"naca63-415.csv")
df_const = pd.read_excel(r'dadosConstantes.xlsx')
df['alfa'] = df['alfa'].astype(float)
df['Cd'] = df['Cd'].astype(float)
df['Cl'] = df['Cl'].astype(float)

list_alfa = df['alfa'].tolist()   ##transformar em listas
list_alfa_2 = list_alfa.copy()
list_Cd = df['Cd'].tolist()
list_Cl = df['Cl'].tolist()

# df_const = pd.DataFrame({'l_C': [1.1375590154884885, 1.0519029878634676, 0.967046897293354, 0.885909960497207, 0.8105468797694305, 0.7420387029339124, 0.6806609507759159, 0.626150945812359, 0.577951383733487, 0.5353846018966951, 0.4977589840166736, 0.4644253645657665, 0.4348017412778228, 0.40837992312551263, 0.38472287001117944, 0.3634578623192851, 0.3442683075723053, 0.32688560675968464, 0.31108172582116783, 0.29666270315794485, 0.28346311557858594, 0.2713414294909357, 0.26017612804267537, 0.24986249864812798, 0.24030997289553374, 0.23143992380949335, 0.22318383963026647, 0.215481806693172, 0.20828124585072108, 0.20153585697251858, 0.19520473445774145, 0.1892516235921462, 0.18364429319875278, 0.1783540045846467, 0.17335506046848814, 0.16862442054876098, 0.16414137277808788, 0.15988725135564585, 0.15584519402811525, 0.15199993257214828],
#                          'l_Solidez': [0.049207461599672986, 0.12381075027044304, 0.17096018328704182, 0.19713233822543125, 0.20867254717728156, 0.21075396087822398, 0.20712766379828665, 0.200309688457676, 0.1918987426905899, 0.1828693685777917, 0.17379318485837555, 0.1649902647931669, 0.15662729975566478, 0.14877932492134352, 0.14146782503937097, 0.13468397629075488, 0.12840268358266618, 0.12259096702574429, 0.11721289632317662, 0.11223242400709539, 0.10761494538170963, 0.10332809223098689, 0.09934207088256491, 0.09562973477048782, 0.0921665076310988, 0.08893022788437953, 0.0859009566285748, 0.08306077431463882, 0.08039358046700927, 0.07788490425326255, 0.07552172971516648, 0.07329233708641206, 0.07118616023185115, 0.06919365946971123, 0.0673062086438322, 0.06551599514780802, 0.06381593157322041, 0.06219957770131113, 0.060661071645164585, 0.05919506905555642],
#                          'l_beta': [63.14640008757691, 58.02386186506133, 52.905437608156156, 47.99693541071314, 43.442665013830656, 39.316858118294526, 35.63711549571336, 32.38465274293049, 29.521831230232706, 27.004078048918487, 24.78678529906782, 22.828739236890627, 21.09346919410594, 19.549475061007126, 18.169914296657126, 16.9320718726865, 15.816780474184753, 14.807870198603123, 13.891679913905005, 13.056638615634743, 12.292913939704516, 11.59212041548622, 10.9470787782863, 10.351617941255867, 9.800412143730126, 9.288846892933137, 8.812908387305585, 8.369092064982706, 7.954326734386047, 7.5659114185250615, 7.201462595414144, 6.858869962548875, 6.536259211875503, 6.231960589378817, 5.9444822441054175, 5.672487556508106, 5.414775784666968, 5.17026548660785, 4.937980273492478, 4.717036526572706],
#                          'l_r': [0.20938139560359614, 0.6281441868107884, 1.0469069780179807, 1.465669769225173, 1.8844325604323653, 2.3031953516395576, 2.72195814284675, 3.140720934053942, 3.5594837252611344, 3.9782465164683267, 4.3970093076755195, 4.815772098882711, 5.234534890089904, 5.653297681297095, 6.072060472504289, 6.49082326371148, 6.909586054918673, 7.328348846125865, 7.747111637333058, 8.16587442854025, 8.584637219747442, 9.003400010954635, 9.422162802161827, 9.840925593369018, 10.259688384576211, 10.678451175783405, 11.097213966990596, 11.515976758197787, 11.93473954940498, 12.353502340612174, 12.772265131819365, 13.191027923026557, 13.60979071423375, 14.028553505440943, 14.447316296648134, 14.866079087855326, 15.284841879062519, 15.703604670269712, 16.1223674614769, 16.541130252684095]})

l_V = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13] ## VELOCIDADES

vel_angular_rotor = 3.66
dif_a = 2
dif_al = 2
df_var = pd.DataFrame(columns=('V', 'Sol', 'r', 'bet', 'fi', 'C', 'Cn', 'Ct', 'Cl', 'Cd', 'a', 'al', 'dif_a', 'dif_al', 'SinCos'))

for V in l_V:
    for i in range(len(df_const['l_r'])):
        a = 0.33
        al = 0.001
        Sol = df_const['l_Solidez'][i]
        r = df_const['l_r'][i]
        C = df_const['l_C'][i]
        bet = df_const['l_beta'][i]
        flag = 0; flag_2 = 0; flag_3 = 0; flag_4 = 0; flag_5 = 0
        while flag != 1:
            den_fi = vel_angular_rotor*r*(1+al) ## denominador do arctan(fi)
            fi = math.atan((1-a)*V/den_fi)

            alfa = math.degrees(fi) - bet
            j = 0
            for k in range(len(list_alfa)): ## Lê os valores de alfa do NACA

                if alfa == list_alfa[k] and flag_2 !=1 and flag_3 !=1: ## Se houver um valor exato ele entra
                    Cn = list_Cl[list_alfa.index(k)]*math.cos(fi) + list_Cd[list_alfa.index(k)]*math.sin(fi)
                    Ct = list_Cl[list_alfa.index(k)]*math.sin(fi) - list_Cd[list_alfa.index(k)]*math.cos(fi)
                    flag_2 = 1
                else:
                    j+=1 ## Soma até o tamanho da lista p/ no if abaixo só entre se tiver lido tds os valores do NACA
                k+=1
            if j==len(list_alfa) and flag_2 != 1 and flag_3 != 1:
                cv_alfa = min(list_alfa, key=lambda x: abs(alfa - x)) ## Pega o valor mais próximo de alfa
                index_2 = list_alfa.index(cv_alfa) - 1 ## pega o 2° valor mais próximo
                #list_alfa_2 = list_alfa.copy()
                #list_alfa_2.pop(list_alfa.index(cv_alfa))
                #cv_alfa_2 = min(list_alfa_2, key=lambda y: abs(alfa - y))

                ## INTERPOLAÇÃO
                Cl_y1 = list_Cl[list_alfa.index(cv_alfa)]
                Cl_y2 = list_Cl[index_2]

                Cd_y1 = list_Cd[list_alfa.index(cv_alfa)]
                Cd_y2 = list_Cd[index_2]

                alfa_x1 = list_alfa[list_alfa.index(cv_alfa)]
                alfa_x2 = list_alfa[index_2]

                R1 = ((alfa - alfa_x2)/(alfa_x1-alfa_x2))

                Cl_int = Cl_y1+(R1*(Cl_y2-Cl_y1))

                R2 = ((alfa - alfa_x2)/(alfa_x1 - alfa_x2))
                Cd_int = Cd_y1+(R2*(Cd_y2-Cd_y1))

                Cn = Cl_int*(math.cos(fi)) + Cd_int*(math.sin(fi))
                Ct = Cl_int*(math.sin(fi)) - Cd_int*(math.cos(fi))
                flag_3 = 1
            if (flag_2 == 1 or flag_3 == 1) and flag != 1: ##

                a_novo = 1/((4*(math.sin(fi) ** 2)/(Sol*Cn))+1)
                dif_a = a - a_novo

                al_novo = 1 / (((4*math.sin(fi)*math.cos(fi))/(Sol*Ct))-1)
                dif_al = al - al_novo

                if dif_a > 0.2:
                    a = a_novo
                else:
                    a = a_novo
                    flag = 1
                    df_var.loc[len(df_var)] = [V, Sol, r, bet, fi, C, Cn, Ct, Cl_int, Cd_int, abs(a), abs(al), abs(dif_a), abs(dif_al), math.sin(fi)*math.cos(fi)]

                if dif_al > 0.2:
                    al = al_novo
                else:
                    al = al_novo
                    flag = 1
                    df_var.loc[len(df_var)] = [V, Sol, r, bet, fi, C, Cn, Ct, Cl_int, Cd_int, abs(a), abs(al), abs(dif_a), abs(dif_al), math.sin(fi)*math.cos(fi)]
    i+=1

df_var['Pot'] = 4.9*(df_var['r']**2)*((df_var['al']*vel_angular_rotor)**2)*df_var['V']*(1-df_var['a'])*df_var['al']*math.pi
df_potbin = df_var.groupby(by='V').sum()
df_potbin = df_potbin.reset_index()

print(df_potbin)
# print(df_var)

writer = pd.ExcelWriter('dados_a_al.xlsx', engine='xlsxwriter')
df_var.to_excel(writer, sheet_name='coeficientes')
writer.close()

plt.bar(df_potbin['V'], df_potbin['Pot'])
plt.show()