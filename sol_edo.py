import numpy as np

def euler(derivative, CI, interval, steps ) -> list:


    min_interval, max_interval = interval

    h = (max_interval - min_interval) / steps

    solution = np.zeros(steps + 1)
    time = np.linspace(min_interval, max_interval,steps+1)

    solution[0] = CI  # Initial condition

    for i in range(0, steps):

        solution[i + 1] = solution[i] + derivative(time[i],solution[i]) * h

    return solution

def RK2(derivative, CI, interval, steps) -> list:

    min_interval, max_interval = interval

    h = (max_interval - min_interval) / steps

    solution = np.zeros(steps + 1)
    time = np.linspace(min_interval, max_interval,steps+1)

    solution[0] = CI  # Initial condition

    for i in range(0,steps):

        k1 = h*derivative( time[i], solution[i] )
        k2 = h*derivative( time[i]+h, (solution[i]) + k1 )
        solution[i+1] = solution[i] + ( (0.5*k1 + 0.5*k2) )

    return solution


def RK4(derivative, CI, interval, steps) -> list:

    min_interval, max_interval = interval

    h = (max_interval - min_interval) / steps

    solution = np.zeros(steps + 1)
    time = np.linspace(min_interval, max_interval,steps+1)

    solution[0] = CI  # Initial condition

    for i in range(0,steps):

        k1 = h*derivative(time[i], solution[i])
        k2 = h*derivative(time[i] + 0.5*h, (solution[i]) + 0.5*k1)
        k3 = h*derivative(time[i] + 0.5*h, (solution[i]) + 0.5*k2)
        k4 = h*derivative(time[i] + h, (solution[i]) + k3)
        solution[i+1] = solution[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)


    return solution






