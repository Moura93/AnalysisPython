import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

freq_angular = 35 #rpm
vel_angular_rotor = (freq_angular / 60) * 2 * math.pi
Vel_desenho = 10
Numero_Pas = 3
potencia_nominal = 400
coeficiente_potencia = 0.3
eficiencia_eletrica = 0.9
velocidade_nominal = 14

df = pd.read_csv('naca63-415.csv')
df['cl/cd'] = abs(df['Cl'])/abs(df['Cd'])

alpha = df['alfa'][df['cl/cd'].idxmax()]
Cl = df['Cl'][df['cl/cd'].idxmax()]
Cd = df['Cd'][df['cl/cd'].idxmax()]

def Calculo_Raio_Rotor(potencia_nominal, coeficiente_potencia, velocidade_nominal, eficiencia_eletrica):
    Densidade_ar = 1.225
    area_transversal = (potencia_nominal * 2 * 1000) / (
            coeficiente_potencia * eficiencia_eletrica * Densidade_ar * velocidade_nominal ** 3)

    R = math.sqrt(area_transversal / math.pi)

    return R

R = Calculo_Raio_Rotor(potencia_nominal, coeficiente_potencia, velocidade_nominal, eficiencia_eletrica)

print(f'O raio é: {R} metros')

Lamb = vel_angular_rotor * R / Vel_desenho

print(f'A razão da velocidade na ponta da pá em relação a velocidade de desenho é: {Lamb}')

l_a = []
l_al = []
l_r = []
l_rR = []
l_C = []
l_CR = []
l_fi = []  # angulo de fluxo
l_Cn = []
l_Ct = []
l_Solidez = []
beta = 0  # angulo de pith
l_beta = []
l_coef = []

iter_max = 100

lamb_loc = 0
l_lamb_loc = []

i = 0
k = 0

for r in np.arange(R / 80, R, R / 40):
    flag = 0
    lamb_loc = vel_angular_rotor * r / Vel_desenho
    l_lamb_loc.append(lamb_loc)
    x = lamb_loc
    l_r.append(r)
    l_rR.append(r / R)
    coef = [16, -24, (9 - 3 * x ** 2), (x ** 2 - 1)]
    l_coef.append(np.roots(coef))

    for k in np.roots(coef):
        flag == 0
        while flag != 1:
            if k <= 1 and k > 0:
                l_a.append(k)
                flag += 1
            else:
                break

for z in l_a:
    al = (1 - 3 * z) / (4 * z - 1)
    l_al.append(al)

for r in np.arange(R / 80, R, R / 40):
    fi = np.arctan(((1 - l_a[i]) * velocidade_nominal) / (vel_angular_rotor * r * (1 + l_al[i])))
    l_fi.append(fi)
    beta = np.degrees(fi) - alpha
    beta = np.radians(beta)
    l_beta.append(beta)
    Cn = Cl * np.cos(fi) + Cd * np.sin(fi)
    l_Cn.append(Cn)
    Ct = Cl * np.sin(fi) - Cd * np.cos(fi)
    l_Ct.append(Ct)
    lamb_loc = vel_angular_rotor * r / Vel_desenho
    C = (8 * r * math.pi * l_a[i] * lamb_loc * (np.sin(fi)) ** 2) / ((1 - l_a[i]) * Numero_Pas * Lamb * Cn)
    Solidez = C * Numero_Pas / (2 * math.pi * r)
    l_Solidez.append(Solidez)
    l_C.append(C)
    l_CR.append(C / r)
    i += 1

print(l_coef)
print(l_a)
print(len(l_a))

print(l_al)
print(len(l_al))

print(l_C)
print(len(l_C))

print(l_Solidez)
print(len(l_Solidez))

print(l_fi)
print(len(l_fi))

print(l_lamb_loc)
print(len(l_lamb_loc))

print(l_beta)
print(len(l_beta))

print(l_r)
print(len(l_r))

# plt.subplot(2, 1, 1)
# plt.plot(l_rR, l_CR)
# plt.xlabel('r/R')
# plt.ylabel('Corda/R')
# plt.title('Corda X R')
# plt.xlim(0.1,1)
# plt.subplot(2, 1, 2)
# plt.plot(l_rR, l_beta)
# plt.xlabel('r/R')
# plt.ylabel('Beta (°)')
# plt.title('Beta º X R')
# plt.xlim(0.1,1)
# plt.tight_layout(pad=0.5)
# plt.show()

df['alfa'] = df['alfa'].astype(float)
df['Cd'] = df['Cd'].astype(float)
df['Cl'] = df['Cl'].astype(float)
l_alfa=[]

i = 0
l_fi2 = []
l_Ct2=[]
l_al_encontrado = []
l_a_encontrado =[]
dif_alfa_1 = 10
list_alfa_2 = []
dif_alfa_2 = 10
Cn = 0
Ct = 0

dif_a = 2
dif_al = 2

l_Cn = []
l_Ct = []
l_C = [0.021578818694310394, 0.16288320788997093, 0.3748535973172071, 0.6051354800561848, 0.8235776087754086, 1.0166351807958582, 1.1808049441879183, 1.317619211423837, 1.4305984642710359, 1.5236712400722345, 1.6004744319955366, 1.6641131766365787, 1.717133943782501, 1.7615827617684794, 1.7990878822547443, 1.8309409048691043, 1.858167005186165, 1.8815823002322987, 1.9018393344873665, 1.9194625971569899, 1.9348760555334943, 1.9484244486356408, 1.960389766046987, 1.9710040335695729, 1.9804592711555606, 1.9889152839911532, 1.9965057889657984, 2.003343257714588, 2.0095227658410204, 2.0151250688990374, 2.020219073725242, 2.024863834509808, 2.0291101733610755, 2.0330020026409823, 2.0365774092319175, 2.0398695478038995, 2.0429073800921707, 2.04571628942985, 2.0483185937568353, 2.050733975631176]
l_Solidez = [0.049207461599672986, 0.12381075027044304, 0.17096018328704182, 0.19713233822543125, 0.20867254717728156, 0.21075396087822398, 0.20712766379828665, 0.200309688457676, 0.1918987426905899, 0.1828693685777917, 0.17379318485837555, 0.1649902647931669, 0.15662729975566478, 0.14877932492134352, 0.14146782503937097, 0.13468397629075488, 0.12840268358266618, 0.12259096702574429, 0.11721289632317662, 0.11223242400709539, 0.10761494538170963, 0.10332809223098689, 0.09934207088256491, 0.09562973477048782, 0.0921665076310988, 0.08893022788437953, 0.0859009566285748, 0.08306077431463882, 0.08039358046700927, 0.07788490425326255, 0.07552172971516648, 0.07329233708641206, 0.07118616023185115, 0.06919365946971123, 0.0673062086438322, 0.06551599514780802, 0.06381593157322041, 0.06219957770131113, 0.060661071645164585, 0.05919506905555642]
l_beta = [63.14640008757691, 58.02386186506133, 52.905437608156156, 47.99693541071314, 43.442665013830656, 39.316858118294526, 35.63711549571336, 32.38465274293049, 29.521831230232706, 27.004078048918487, 24.78678529906782, 22.828739236890627, 21.09346919410594, 19.549475061007126, 18.169914296657126, 16.9320718726865, 15.816780474184753, 14.807870198603123, 13.891679913905005, 13.056638615634743, 12.292913939704516, 11.59212041548622, 10.9470787782863, 10.351617941255867, 9.800412143730126, 9.288846892933137, 8.812908387305585, 8.369092064982706, 7.954326734386047, 7.5659114185250615, 7.201462595414144, 6.858869962548875, 6.536259211875503, 6.231960589378817, 5.9444822441054175, 5.672487556508106, 5.414775784666968, 5.17026548660785, 4.937980273492478, 4.717036526572706]
l_r = [0.20938139560359614, 0.6281441868107884, 1.0469069780179807, 1.465669769225173, 1.8844325604323653, 2.3031953516395576, 2.72195814284675, 3.140720934053942, 3.5594837252611344, 3.9782465164683267, 4.3970093076755195, 4.815772098882711, 5.234534890089904, 5.653297681297095, 6.072060472504289, 6.49082326371148, 6.909586054918673, 7.328348846125865, 7.747111637333058, 8.16587442854025, 8.584637219747442, 9.003400010954635, 9.422162802161827, 9.840925593369018, 10.259688384576211, 10.678451175783405, 11.097213966990596, 11.515976758197787, 11.93473954940498, 12.353502340612174, 12.772265131819365, 13.191027923026557, 13.60979071423375, 14.028553505440943, 14.447316296648134, 14.866079087855326, 15.284841879062519, 15.703604670269712, 16.1223674614769, 16.541130252684095]

list_alfa = df['alfa'].tolist()

list_Cd = df['Cd'].tolist()
list_Cl = df['Cl'].tolist()
l_v = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
l_cv_alfa = []
l_cv_alfa_2 = []
z = 0

for r in l_r:
    a = 0.30
    al = 0.001
    Sol = l_Solidez[i]
    bet = l_beta[i]
    Cor = l_C[i]
    flag = 0

        # Objetivo: Para cada Fi calcular o angulo alfa, caso esse angulo esteja no arquivo Naca, ler o Cd Cl e
        # calcular o Cn Ct. Caso não tenha, fazer uma interpolação com os valores mais próximos.
        # Com o Cn e Ct, calcular um a e a' até que a diferença entre as duas ultimas iterações seja menor que
        # determinado limite

    while flag!=1:
        fi= np.arctan(((1-a)*l_v[z])/(vel_angular_rotor*r*(1+al)))
        fi = np.degrees(fi)
        alfa = fi - bet
        l_alfa.append(alfa)
        list_alfa_2 =list_alfa.copy()
        flag_2 = 0
        flag_3=0
        j=0
        flag_4 = 0
        flag_5 = 0
        for valor in list_alfa:
            if  valor == alfa:
                Cn = list_Cl(list_alfa.index(valor))*np.cos(np.radians(fi)) + list_Cd(list_alfa.index(valor))*np.sin(np.radians(fi))
                Ct = list_Cl(list_alfa.index(valor))*np.sin(np.radians(fi)) - list_Cd(list_alfa.index(valor))*np.cos(np.radians(fi))
                flag_2=1
            else:
                j+=1
        if (j==len(list_alfa) and flag_2 !=1)or flag_3!=1:
            alfa_inteiro = round(alfa,0)
            cv_alfa = min(list_alfa, key=lambda x: abs(alfa - x))
            list_alfa_2 = list_alfa
            list_alfa_2.pop(list_alfa.index(cv_alfa))
            cv_alfa_2 = min(list_alfa_2, key=lambda x: abs(alfa - x))
            Cl_y1 = list_Cl[list_alfa.index(cv_alfa)]
            Cl_y2 = list_Cl[list_alfa_2.index(cv_alfa_2)]
            Cd_y1 = list_Cd[list_alfa.index(cv_alfa)]
            Cd_y2 = list_Cd[list_alfa_2.index(cv_alfa_2)]
            alfa_x1 = list_alfa[list_alfa.index(cv_alfa)]
            alfa_x2 = list_alfa[list_alfa_2.index(cv_alfa_2)]
            div_Cl = (alfa_x1 - alfa_x2)
            div_Cd = (alfa_x1 - alfa_x2)
            print(f"Div Cl: {div_Cl} \n Div Cd: {div_Cd}")
            Cl_int = Cl_y1 + (((alfa - alfa_x2) / div_Cl) * (Cl_y2 - Cl_y1))
            Cd_int = Cd_y1 + (((alfa - alfa_x2) / div_Cd) * (Cd_y2 - Cd_y1))
            Cn = Cl_int*np.cos(np.radians(fi)) + Cd_int*np.sin(np.radians(fi))
            Ct = Cl_int*np.sin(np.radians(fi)) - Cd_int*np.cos(np.radians(fi))
            flag_3 = 1
        if flag !=1 and(flag_2 ==1 or flag_3==1):
            novo_a = (1/(((4*(np.sin(np.radians(fi)))**2)/(Sol*Cn)) + 1))
            novo_al= (1/(((4*((np.sin(np.radians(fi)))*(np.cos(np.radians(fi)))))/(Sol*Ct))-1))
            dif_a= (abs(novo_a) - abs(a))/abs(a)
            dif_al= abs(novo_al) - abs(al)/abs(al)
            a = novo_a
            al = novo_al
    if dif_a<=0.01 and flag_4!=1:
        l_a_encontrado.append(a)
        flag_4 = 1
    if dif_al<=0.01 and flag_5 !=1:
        l_al_encontrado.append(al)
        flag_5=1
    if flag_4==1 and flag_5==1:
        flag = 1
        l_Cn.append(Cn)
        l_Ct2.append(Ct)
        l_cv_alfa.append(cv_alfa)
        l_cv_alfa_2.append(cv_alfa_2)
        l_fi2.append(fi)
        l_alfa.append(alfa)
    i+=1

print(f'a encontrado: {l_a_encontrado}')
print(len(l_a_encontrado))
print(f'al encontrado: {l_al_encontrado}')
print(len(l_al_encontrado))
print(f'Cn encontrado: {l_Cn}')
print(len(l_Cn))
print(f'Ct encontrado: {l_Ct2}')
print(len(l_Ct2))

print(f'Fi encontrado: {l_fi2}')
print(len(l_fi2))

print(F'Angulo alfa 1: {l_cv_alfa}')
print(len(l_cv_alfa))
print(F'Angulo alfa 2: {l_cv_alfa_2}')
print(len(l_cv_alfa_2))

vel_angular_rotor
M = 0
l_dM = []
l_M = []
l_Pot = []
l_Vo= [4,5,6,7,8,9,10,11,12,13,14]
z = 0
for Vo in l_Vo:
    i = 0
    M=0
    for r in l_r:
        al = l_al_encontrado[i]
        #al=0.001
        w = a*vel_angular_rotor
        #w=al*vel_angular_rotor
        a = l_a_encontrado[i]
        #a = 0.3
        C = l_C[i]
        Ct = l_Ct2[i]
        fi = l_fi2[i]
        i+=1
        dM = (1/2)*((1.225)*3*Vo*(1-a)**r*(1+al)*C*Ct*r*(R/40))/(np.sin(np.radians(fi))*np.cos(np.radians(fi)))
        l_dM.append(dM)
        M += dM
    l_M.append(M)
    Pot = M*vel_angular_rotor
    l_Pot.append(Pot)
print(l_Pot)
print(len(l_M))

plt.plot(l_Pot, l_Vo)
plt.show()