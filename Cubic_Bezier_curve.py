import numpy as np 
import matplotlib.pyplot as plt

def main():
    p0 = np.array([10,30])

    x = [p0[0]]
    y = [p0[1]]

    p1 = np.array([50,20])
    p2 = np.array([60,70])
    p3 = np.array([20, 20])

    t = 0
    speed = 0.01

    while(t<1):
        t += speed

        P0_x = pow((1-t), 3) * p0[0]
        P0_y = pow((1-t), 3) * p0[1]

        P1_x = 3 * pow((1-t), 2) * t * p1[0]
        P1_y = 3 * pow((1-t), 2) * t * p1[1]

        P2_x = 3 * (1-t) * pow(t, 2) * p2[0]
        P2_y = 3 * (1-t) * pow(t, 2) * p2[1]

        P3_x = pow(t, 3) * p3[0]
        P3_y = pow(t, 3) * p3[1]

        x.append(P0_x + P1_x + P2_x + P3_x)
        y.append(P0_y + P1_y + P2_y + P3_y)

    plt.plot(x, y)
    plt.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], 'o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cubic Bezier Curve')
    plt.show()

main()    