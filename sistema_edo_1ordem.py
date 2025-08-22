import numpy as np
import matplotlib.pyplot as plt


g = 9.81
cd = 0.25
m = 68.1


#edos
def dxdt(t, x, v):
    return v


def dvdt(t, x, v):
    return g - (cd/m)*(v**2)


#analitica
def va(t):
    return (((g*m)/cd)**(1/2)) * np.tanh((((g*cd)/m)**(1/2))*t)

def xa(t):
    return (m/cd) * np.log(np.cosh(np.sqrt(g*cd/m)*t))


#min interval, max interval
a, b = [0, 10]

#number of steps
n = 20

#step size
h = (b - a) / n

#vetores soluções
t = np.linspace(a,b,n)
x = np.zeros(n)
v = np.zeros(n)

#vetor pro erro
Ept = np.zeros(n)

#initial conditions
x[0] = 0
v[0] = 0


for i in range(0, n-1):
    x[i + 1] = x[i] + h*dxdt(t[i], x[i], v[i])
    v[i + 1] = v[i] + h*dvdt(t[i], x[i], v[i])


print("DX/DT")
print(x)
print("DV/DT")
print(t)


# gráfico comparativo entre metodos numericos e soluções analiticas
plt.plot(t,x,'ob',label='dx/dt')
plt.plot(t,v,'ob',label='dv/dt')
plt.plot(t,va(t),'--og',label='Analítica v(t)')
plt.plot(t,xa(t),'--og',label='Analítica x(t)')
#plt.plot(t, Ept,'or',label='Erro Percentual Verdadeiro')
plt.legend()
plt.grid()
plt.show()