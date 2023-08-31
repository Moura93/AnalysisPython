# -*- coding: utf-8 -*-
import pandas as pd
import math 
import numpy as np


vel_angular_rotor = (35/60)*2*math.pi
Vel_desenho = 9
Numero_Pas = 3
def Calculo_Raio_Rotor(potencia_nominal, coeficiente_potencia, velocidade_nominal, eficiencia_eletrica):
    Densidade_ar = 1.225
    area_transversal = (potencia_nominal * 2 * 1000) / (
                coeficiente_potencia * eficiencia_eletrica * Densidade_ar * velocidade_nominal ** 3)

    Raio = math.sqrt(area_transversal / math.pi)

    return Raio


potencia_nominal = float(input('Insira a potência nominal(kw): '))
coeficiente_potencia = float(input('Insira o coeficiente nominal: '))
eficiencia_eletrica = float(input('Insira a eficiência elétrica do aerogerador: '))

velocidade_nominal = float(input('Insira a velocidade nominal: '))

Raio_rotor = Calculo_Raio_Rotor(potencia_nominal, coeficiente_potencia, velocidade_nominal, eficiencia_eletrica)

print(f'O raio é: {Raio_rotor} metros')

Tip_speed_ratio = vel_angular_rotor* Raio_rotor/Vel_desenho

print(f'A razão da velocidade na ponta da pá em relação a velocidade de desenho é: {Tip_speed_ratio}')

Coeficiente_linear_a = 0.3
Coeficiente_tang_alinha = 0
Lista_Coeficiente_Linear_a = []
Lista_Coeficiente_tang_alinha = []
seccao_raio = Raio_rotor/40
Coef_Lift = 0.7
Coef_Drag = 0.3

Lista_Corda = []
Lista_seccao_raio = []
i = 0
Aux_1 = 0
dif_coeficiente_linear = 5
dif_coeficiente_tang = 5
seccao_raio_iter = 0


while i < 40:
#Fator_f = (Numero_Pas/2)*(Raio_rotor-seccao_raio_iter)/(seccao_raio_iter*math.sen(ang_fluxo))
#Fator_F = (2/math.pi)*(math.acos(math.e**(-Fator_f)))
    try:
        x = vel_angular_rotor*seccao_raio_iter/Vel_desenho #Ver se V0 é desenho ou nominal
        ang_fluxo = math.atan(((1-Coeficiente_linear_a)*velocidade_nominal)/(vel_angular_rotor*Raio_rotor*(1+Coeficiente_tang_alinha)))
        seccao_raio_iter = seccao_raio*0.5 + i*(seccao_raio)
 
        Coef_Normal = Coef_Lift*math.cos(ang_fluxo) +Coef_Drag*math.sin(ang_fluxo)
        Coef_Tangecial = Coef_Lift*math.sin(ang_fluxo) - Coef_Drag*math.cos(ang_fluxo)

        Corda_iter = (Raio_rotor*8*math.pi*Coeficiente_linear_a*x*(math.sin(ang_fluxo)**2))/((1-Coeficiente_linear_a)*Numero_Pas*Tip_speed_ratio*Coef_Normal)#Ver se Coef_Normal é o optimal ou é esse


        Solidez_Local = Numero_Pas*Corda_iter/(2*math.pi*seccao_raio_iter)
    
        print(f'o angulo de fluxo é {ang_fluxo} {i}')
    
        i =i+1
        Aux_1 = Aux_1+1

    
        Coeficiente_linear_a = 1/((4*(math.sin(ang_fluxo)*math.cos(ang_fluxo))/Solidez_Local*Coef_Tangecial)-1)
        Lista_Coeficiente_Linear_a.append(Coeficiente_linear_a)
        
        Coeficiente_tang_alinha = 1/((4*(math.sin(ang_fluxo)**2)/Solidez_Local*Coef_Normal)+1)
        Lista_Coeficiente_tang_alinha.append(Coeficiente_tang_alinha)
        
        Lista_Corda.append(Corda_iter)

        Lista_seccao_raio.append(seccao_raio_iter)
    except ZeroDivisionError:
        print('Algo foi dividido por zero')
    
        if i >1:
            while dif_coeficiente_linear<=0.1 & dif_coeficiente_tang<=0.1:
                dif_coeficiente_linear=(abs(Lista_Coeficiente_Linear_a[i])-abs(Lista_Coeficiente_Linear_a[i-1]))/abs(Lista_Coeficiente_linear_a[i-1])
                dif_coeficiente_tang=(abs(Lista_Coeficiente_tang_alinha[i])-abs(Lista_Coeficiente_tang_alinha[i-1]))/abs(Lista_Coeficiente_tang_alinha[i-1])
        
                if dif_coeficiente_linear<=0.1 & dif_coeficiente_tang<=0.1:
                    print(f'O coeficiente Linear a foi:''{Coeficiente_linear_a}')
                    print(f'O Coeficiente tangencial a' 'Foi:{Coeficiente_tang_alinha}')
                    break
        
            

print(f'Os raios de cada secção é: {Lista_seccao_raio}')

print(f'A corda de cada secção é: {Lista_Corda}')

