import numpy as np
import matplotlib.pyplot as plt

def euler(derivative, CI, interval, steps ) -> list:


    min_interval, max_interval = interval

    h = (max_interval - min_interval) / steps

    solution = np.zeros(steps + 1)
    time = np.linspace(min_interval, max_interval,steps+1)

    solution[0] = CI  # Initial condition

    for i in range(0, steps):

        solution[i + 1] = solution[i] + derivative(time[i],solution[i]) * h

    return solution



if __name__ == '__main__':

    def f(t,y,):

        return  4*np.exp(0.8*t) - 0.5*y
    
    def funciton(t):
        return (4/1.3)*(np.exp(0.8*t) - np.exp(-0.5*t)) + (2*np.exp(-0.5*t))

    n = 100
    x_values = np.linspace(0,4,n+1)
    y_values = [funciton(x) for x in x_values]

    custom_style = {
            'font.size': 12,
            'axes.labelsize': 14,
            'axes.titlesize': 16,
            'axes.linewidth': 1.5,
            'xtick.labelsize': 12,
            'ytick.labelsize': 12,
            'lines.linewidth': 2,
            'lines.markersize': 6,
            'legend.fontsize': 12,
            'legend.frameon': False,
            'legend.loc': 'best',
            'figure.figsize': (8, 6),
            'savefig.dpi': 600,
            'savefig.bbox': 'tight',
        }
    
    plt.style.use(custom_style)
    
    euler_solution = euler(f,2,[0,4],n)
    plt.plot(x_values, y_values,'o',color='k',markersize = 4.5, label='Analytical solution')
    plt.plot(x_values, euler_solution,color = 'r', label='Euler solution')
    plt.margins(0.1,0.1)
    plt.legend()
    plt.grid()
    plt.show()