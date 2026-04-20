import numpy as np
from scipy.integrate import odeint

def simulate():
    m, c, k = 1, 0.5, 4

    def model(y, t):
        x, v = y
        return [v, -(c/m)*v - (k/m)*x]

    t = np.linspace(0, 10, 1000)
    sol = odeint(model, [1, 0], t)

    return t, sol[:,0]
