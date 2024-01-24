import numpy as np
import matplotlib.pyplot as plt

def main():
    a = [100]
    b = [50]
    c = [0]

    k1, k2= 0.008, 0.002
    dt = 0.1 

    totalStep = 100
    t = [0]

    for i in range(totalStep):

        t_a = a[-1]
        t_b = b[-1]
        t_c = c[-1]
        t_t = t[-1]

        a.append(t_a + (k2 * t_c - k1*t_a*t_b) * dt)
        b.append(t_b + (k2 * t_c - k1*t_a*t_b) * dt)
        c.append(t_c + (2*k1*t_a*t_b - 2*k2*t_c) * dt)
        t.append(t_t+dt)

    

    print('Time\t A(i)\t C(i)\tC(i)')

    for i in range(totalStep+1):

        print(np.round(t[i],2),'\t', np.round(a[i],2),'\t',np.round(b[i],2),'\t',np.round(c[i],2))


main()    