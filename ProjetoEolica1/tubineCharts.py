import numpy as np
import matplotlib.pyplot as plt

# CONSTANTES
p = 1.2754 #kg/m³ densidade do ar
r = 30 #m raio do rotor

# CÁLCULOS
A = np.pi*r**2 # Área do rotor
a = np.linspace(0,1,100) # Coeficiente de indução axial
Cp = 4*a*(1-a)**2
Ct = 4*a*(1-a)

Vo = np.linspace(0,10,100) # Velocidade do vento de entrada
u1 = np.linspace(0,10,100) # Velocidade do vento de saída
u = (Vo+u1)/2 # Velocidade do vento no rotor

a = np.linspace(0.255,1/3,100) # Axial induction factor
a1 = np.divide((1-(3*a)),((4*a)-1)) # Coeficiente de indução tangencial
parte_um = np.multiply(a,(1-a))
parte_dois = np.multiply(a1,(1+a1))
divisao = np.divide(parte_um,parte_dois)
x = np.sqrt(divisao) # local rotation speed

# PLOTAGEM DOS GRÁFICOS
fig, ax = plt.subplots(2,2)

# Cp e Ct
ax[0,0].plot(a,Ct)
ax[0,0].plot(a,Cp)
ax[0,0].grid()
ax[0,0].legend(['Thrust Coefficient','Power Coefficient'])
ax[0,0].set_xlabel('a')
ax[0,0].set_ylabel('Ct, Cp')

# a' / a
ax[0,1].plot(a,a1)
ax[0,1].grid()
ax[0,1].legend(["a' [ω/Ω]"])
ax[0,1].set_xlabel('a [μa/μ1]')
ax[0,1].set_ylabel("a'")

# x / a
ax[1,1].plot(a,x, color='r')
ax[1,1].grid()
ax[1,1].legend(['x'])
ax[1,1].set_xlabel('a [μa/μ1]')
ax[1,1].set_ylabel('x')

plt.show()