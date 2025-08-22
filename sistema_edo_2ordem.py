import numpy as np
import matplotlib.pyplot as plt

# v =  dy/dt
# d²y/dt = dv/dt

def dydt(t, y, v):
    return v

def dvdt(t, y, v):
    return -k * y

def anal(t):
  return np.cos(np.sqrt(k) * t) + (1/np.sqrt(k)) * np.sin(np.sqrt(k) * t)

k = 1

#min interval, max interval
a, b = [0, 4]

#number of steps
n = 100

#step size
h = (b - a) / n

#vetores soluções
t = np.linspace(a,b,n)
y = np.zeros(n)
v = np.zeros(n)

#vetor pro erro
Ept = np.zeros(n)

#initial conditions
y[0] = 1
v[0] = 1


for i in range(0, n-1):
    y[i + 1] = y[i] + h * dydt(t[i], y[i], v[i])
    v[i + 1] = v[i] + h * dvdt(t[i], y[i], v[i])


print("DX/DT")
print(y)
print("DV/DT")
print(t)


# gráfico comparativo entre metodos numericos e soluções analiticas
plt.plot(t,y,'ob',label='dy/dt = v')
plt.plot(t,v,'ob',label='dv/dt = y²')
plt.plot(t,anal(t),'--og',label='Analítica v(t)')
#plt.plot(t,xa(t),'--og',label='Analítica x(t)')
#plt.plot(t, Ept,'or',label='Erro Percentual Verdadeiro')
plt.legend()
plt.grid()
plt.show()