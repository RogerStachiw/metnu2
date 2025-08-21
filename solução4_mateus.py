import numpy as np
import matplotlib.pyplot as plt
import time as time

def derivative_1 (t,T,C):

    return -np.exp(-10/(T+273))*C

def derivative_2 (t,T,C):

    return 1000*np.exp(-10/(T+273))*C  - 10*(T - 20)

min_interval, max_interval = [0,10]
n = 45
h = (max_interval - min_interval) / n

solution_T_rk4 = np.zeros(n + 1)
solution_C_rk4 = np.zeros(n + 1)
time = np.linspace(min_interval, max_interval,n+1)

solution_T_rk4[0] = 16

solution_C_rk4[0] = 1  # Initial condition

for i in range(0,n):

    k1_C = h*derivative_1(time[i], solution_T_rk4[i], solution_C_rk4[i])
    k1_T = h*derivative_2(time[i], solution_T_rk4[i], solution_C_rk4[i])

    k2_C = h*derivative_1(time[i] + 0.5*h, (solution_T_rk4[i]) + 0.5*k1_T, solution_C_rk4[i]+ 0.5*k1_C)
    k2_T = h*derivative_2(time[i] + 0.5*h, (solution_T_rk4[i]) + 0.5*k1_T, solution_C_rk4[i]+ 0.5*k1_C)

    k3_C = h*derivative_1(time[i] + 0.5*h, (solution_T_rk4[i]) + 0.5*k2_T, solution_C_rk4[i]+ 0.5*k2_C)
    k3_T = h*derivative_2(time[i] + 0.5*h, (solution_T_rk4[i]) + 0.5*k2_T, solution_C_rk4[i]+ 0.5*k2_C)

    k4_C = h*derivative_1(time[i] + h, (solution_T_rk4[i]) + k3_T, solution_C_rk4[i]+ k3_C)
    k4_T = h*derivative_2(time[i] + h, (solution_T_rk4[i]) + k3_T, solution_C_rk4[i]+ k3_C)

    solution_C_rk4[i+1] = solution_C_rk4[i] + (1/6)*(k1_C + 2*k2_C + 2*k3_C + k4_C)
    solution_T_rk4[i+1] = solution_T_rk4[i] + (1/6)*(k1_T + 2*k2_T + 2*k3_T + k4_T)


solution_T_euler = np.zeros(n + 1)
solution_C_euler = np.zeros(n + 1)
time = np.linspace(min_interval, max_interval, n + 1)

solution_T_euler[0] = 16
solution_C_euler[0] = 1  # Initial condition

for i in range(0, n):
    solution_C_euler[i + 1] = solution_C_euler[i] + h * derivative_1(time[i], solution_T_euler[i], solution_C_euler[i])
    solution_T_euler[i + 1] = solution_T_euler [i] +h * derivative_2(time[i], solution_T_euler[i], solution_C_euler[i])



solution_T_rk2 = np.zeros(n + 1)
solution_C_rk2 = np.zeros(n + 1)
time = np.linspace(min_interval, max_interval, n + 1)

solution_T_rk2[0] = 16
solution_C_rk2[0] = 1  # Initial condition

for i in range(0, n):

    k1_C = h*derivative_1(time[i], solution_T_rk2[i], solution_C_rk2[i])
    k1_T = h*derivative_2(time[i], solution_T_rk2[i], solution_C_rk2[i])

    k2_C = h*derivative_1(time[i] + h, (solution_T_rk2[i]) + k1_T, solution_C_rk2[i]+ k1_C)
    k2_T = h*derivative_2(time[i] + h, (solution_T_rk2[i]) + k1_T, solution_C_rk2[i]+ k1_C)

    solution_C_rk2[i + 1] = solution_C_rk2[i] + (0.5 * k1_C + 0.5 * k2_C)
    solution_T_rk2[i + 1] = solution_T_rk2[i] + (0.5 * k1_T + 0.5 * k2_T)
    




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

plt.plot(time,solution_C_rk4,'o--', color='#27ae60', label='RK4')
plt.plot(time,solution_C_rk2, 'o--', color='#2980b9', label='RK2')
plt.plot(time,solution_C_euler,'o--', color='#e74c3c', label='Euler')
plt.title(f'Soluções para passo de {h}')
plt.margins(0.1, 0.1)
plt.xlabel('Tempo')
plt.ylabel('Concentração')
plt.legend()
plt.savefig(f'4_Solutions for step of {h} (concetration).pdf',format='pdf')
plt.show()



plt.plot(time,solution_T_rk4,'o--', color='#27ae60', label='RK4')
plt.plot(time,solution_T_rk2, 'o--', color='#2980b9', label='RK2')
plt.plot(time,solution_T_euler,'o--', color='#e74c3c', label='Euler')
plt.title(f'Soluções para passo de {h}')
plt.xlabel('Tempo')
plt.ylabel('Temperatura')
plt.margins(0.1, 0.1)
plt.legend()
plt.savefig(f' 4- Solutions for step of {h} (temperature).pdf',format='pdf')
plt.show()