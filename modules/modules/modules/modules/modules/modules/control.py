import numpy as np

def simulate():
    Kp, Ki, Kd = 10, 1, 2
    dt = 0.01
    t = np.arange(0, 10, dt)

    x, v = 0, 0
    ref = 1
    erro_int = 0
    erro_ant = 0

    xs = []

    for _ in t:
        erro = ref - x
        erro_int += erro*dt
        erro_der = (erro - erro_ant)/dt

        u = Kp*erro + Ki*erro_int + Kd*erro_der

        v += u*dt
        x += v*dt

        xs.append(x)
        erro_ant = erro

    return t, xs
