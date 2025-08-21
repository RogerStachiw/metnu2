import numpy as np
import matplotlib.pyplot as plt
from sol_edo import *


def analytical_equation(t):
    return np.exp( (t**4)/4 - (1.5)*t)


def derivative(t, y):
    return y*t**3 - 1.5*y


def error_percentage(solution,approximately):

    error = []

    for i in range(len(solution)):
        e = np.abs((solution[i] - approximately[i])/(solution[i]))*100
        error.append(e)

    
    return error



euler_solution_0_5 = euler(derivative,1,[0,2],4)
euler_solution_0_25 = euler(derivative,1,[0,2],8)
euler_solution_0_01 = euler(derivative,1,[0,2],200)



RK2_solution_0_5 = RK2(derivative,1,[0,2],4)
RK2_solution_0_25 = RK2(derivative,1,[0,2],8)
RK2_solution_0_01 = RK2(derivative,1,[0,2],200)



RK4_solution_0_5 = RK4(derivative,1,[0,2],4)
RK4_solution_0_25 = RK4(derivative,1,[0,2],8)
RK4_solution_0_01 = RK2(derivative,1,[0,2],200)




custom_style = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans', 'Helvetica'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'axes.linewidth': 1.2,
    'axes.grid': True,
    'grid.alpha': 0.7,
    'grid.linewidth': 0.8,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 5.0,
    'xtick.minor.size': 3.0,
    'ytick.major.size': 5.0,
    'ytick.minor.size': 3.0,
    'lines.linewidth': 2.2,
    'lines.markersize': 8,
    'lines.markeredgewidth': 1,
    'legend.fontsize': 11,
    'legend.frameon': True,
    'legend.framealpha': 0.9,
    'legend.edgecolor': 'black',
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'figure.autolayout': True,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.transparent': False,
    'axes.prop_cycle': plt.cycler('color', plt.cm.tab10.colors),
    'image.cmap': 'viridis',
    'axes.edgecolor': 'black',
    'axes.labelcolor': 'black',
}
plt.style.use(custom_style)

################################################################################



x_values = np.linspace(0,2,5)
x_values_an = np.linspace(0,2,1000)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

ax1.plot(x_values_an, analytical_equation(x_values_an), color='#2c3e50', label='Solução Analítica', zorder=3)
ax1.plot(x_values, euler_solution_0_5, 'o--', color='#e74c3c', lw=2.5, label='Euler')
ax1.plot(x_values, RK2_solution_0_5, 'o--', color='#2980b9', lw=2.5, label='RK2')
ax1.plot(x_values, RK4_solution_0_5, 'o--', color='#27ae60', lw=2.5, label='RK4')
ax1.margins(0.1, 0.1)
ax1.set_title('Soluções para o passo de 0.5')
ax1.set_xlabel('Tempo')
ax1.set_ylabel('y(t)')
ax1.legend()



a =analytical_equation(x_values)

error_euler = error_percentage(a,euler_solution_0_5)
error_rk2 = error_percentage(a,RK2_solution_0_5)
error_rk4 = error_percentage(a,RK4_solution_0_5)
error_medio_euler = sum(error_euler)/len(euler_solution_0_5)
print(f'Erro medio Euler para o passo de 0.5: {round(error_medio_euler,2)}%')
error_medio_rk2 = sum(error_rk2)/len(RK2_solution_0_5)
print(f'Erro medio RK2 para o passo de 0.5: {round(error_medio_rk2,2)}%')
error_medio_rk4 = sum(error_rk4)/len(RK4_solution_0_5)
print(f'Erro medio RK4 para o passo de 0.5: {round(error_medio_rk4,2)}%')
ax2.plot(x_values, error_euler, 'o--', color='#e74c3c', label='Euler')
ax2.plot(x_values, error_rk2, 'o--', color='#2980b9', label='RK2')
ax2.plot(x_values, error_rk4, 'o--', color='#27ae60', label='RK4')
ax2.set_title('Erros para o passo de 0.5')
ax2.set_xlabel('Tempo')
ax2.set_ylabel('y(t)')
ax2.set_ylabel('Erros (%)')
ax2.margins(0.1, 0.1)
ax2.legend(loc='upper left')
plt.savefig(' 1- Solutions for step of 0.5.pdf',format='pdf')
plt.show()


#################################################################################

x_values = np.linspace(0,2,9)



a =analytical_equation(x_values)

error_euler = error_percentage(a,euler_solution_0_25)
error_rk2 = error_percentage(a,RK2_solution_0_25)
error_rk4 = error_percentage(a,RK4_solution_0_25)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

ax1.plot(x_values_an, analytical_equation(x_values_an), color='#2c3e50', label='Solução Analítica', zorder=3)
ax1.plot(x_values, euler_solution_0_25, 'o--', color='#e74c3c', lw=2.5, label='Euler')
ax1.plot(x_values, RK2_solution_0_25, 'o--', color='#2980b9', lw=2.5, label='RK2')
ax1.plot(x_values, RK4_solution_0_25, 'o--', color='#27ae60', lw=2.5, label='RK4')
error_medio_euler = sum(error_euler)/len(euler_solution_0_25)
print(f'Erro medio Euler para o passo de 0.25: {round(error_medio_euler,2)}%')
error_medio_rk2 = sum(error_rk2)/len(RK2_solution_0_25)
print(f'Erro medio RK2 para o passo de 0.25: {round(error_medio_rk2,2)}%')
error_medio_rk4 = sum(error_rk4)/len(RK4_solution_0_25)
print(f'Erro medio RK4 para o passo de 0.25: {round(error_medio_rk4,2)}%')


ax1.margins(0.1, 0.1)
ax1.set_title('Soluções para o passo de 0.25')
ax1.set_xlabel('Tempo')
ax1.set_ylabel('y(t)')
ax1.legend()

ax2.plot(x_values, error_euler, 'o--', color='#e74c3c', label='Euler')
ax2.plot(x_values, error_rk2, 'o--', color='#2980b9', label='RK2')
ax2.plot(x_values, error_rk4, 'o--', color='#27ae60', label='RK4')
ax2.set_title('Erros para o passo de 0.25')
ax2.set_xlabel('Tempo')
ax2.set_ylabel('Erros (%)')
ax2.margins(0.1, 0.1)
ax2.legend(loc='upper left')
plt.savefig(' 1- Solutions for step of 0.25.pdf',format='pdf')
plt.show()


# #################################################################################

x_values = np.linspace(0,2,201)



a =analytical_equation(x_values)

error_euler = error_percentage(a,euler_solution_0_01)
error_rk2 = error_percentage(a,RK2_solution_0_01)
error_rk4 = error_percentage(a,RK4_solution_0_01)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

ax1.plot(x_values_an, analytical_equation(x_values_an), color='#2c3e50', label='Solução Analítica', zorder=3)
ax1.plot(x_values, euler_solution_0_01, 'o--', color='#e74c3c', lw=2.5, label='Euler')
ax1.plot(x_values, RK2_solution_0_01, 'o--', color='#2980b9', lw=2.5, label='RK2')
ax1.plot(x_values, RK4_solution_0_01, 'o--', color='#27ae60', lw=2.5, label='RK4')
ax1.margins(0.1, 0.1)
ax1.set_title('Soluções para o passo de 0.01')
ax1.set_xlabel('Tempo')
ax1.set_ylabel('y(t)')
ax1.legend()

error_medio_euler = sum(error_euler)/len(euler_solution_0_01)
print(f'Erro medio Euler para o passo de 0.01: {round(error_medio_euler,2)}%')
error_medio_rk2 = sum(error_rk2)/len(RK2_solution_0_01)
print(f'Erro medio RK2 para o passo de 0.01: {round(error_medio_rk2,2)}%')
error_medio_rk4 = sum(error_rk4)/len(RK4_solution_0_01)
print(f'Erro medio RK4 para o passo de 0.01: {round(error_medio_rk4,2)}%')



ax2.plot(x_values, error_euler, 'o--', color='#e74c3c', label='Euler')
ax2.plot(x_values, error_rk2, 'o--', color='#2980b9', label='RK2')
ax2.plot(x_values, error_rk4, 'o--', color='#27ae60', label='RK4')
ax2.set_title('Erros para o passo de 0.01')
ax2.set_xlabel('Tempo')
ax2.set_ylabel('Erros (%)')
ax2.margins(0.1, 0.1)
ax2.legend(loc='upper left')
plt.savefig(' 1- Solutions for step of 0.01.pdf',format='pdf')
plt.show()
# 
#################################################################################