import numpy as np

def simulate():
    nx = 50
    T = np.zeros(nx)
    T[20:30] = 100

    for _ in range(200):
        Tn = T.copy()
        for i in range(1, nx-1):
            T[i] = Tn[i] + 0.01*(Tn[i+1] - 2*Tn[i] + Tn[i-1])

    return T
