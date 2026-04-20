import numpy as np

def simulate():
    r, l = 1, 3
    theta = np.linspace(0, 2*np.pi, 200)
    x = r*np.cos(theta) + np.sqrt(l**2 - (r*np.sin(theta))**2)
    return theta, x
