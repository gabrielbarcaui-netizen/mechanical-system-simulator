import numpy as np

def simulate():
    m, F, cd = 1200, 4000, 0.3
    dt = 0.01
    t = np.arange(0, 20, dt)
    v = np.zeros(len(t))

    for i in range(1, len(t)):
        v[i] = v[i-1] + ((F - cd*v[i-1]**2)/m)*dt

    return t, v
