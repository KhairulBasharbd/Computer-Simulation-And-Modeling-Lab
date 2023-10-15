# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


A = [1.0]       # Initial concentration of A: 1.0 mole per liter
B = [0.5]       # Initial concentration of B: 0.5 mole per liter
C = [0.0]       # Initial concentration of C: 0.5 mole per liter



total_time = 100
steps = 500
k1 = k2 = 0.05
t = dt = total_time / steps
time = [t]

figure, axis = plt.subplots()


axis.set_xlim(0, total_time)
axis.set_ylim(0, max(A[-1], B[-1]))

line_A, = axis.plot([], label="A", color="black")
line_B, = axis.plot([], label="B", color='green')
line_C, = axis.plot([], label="C", color='blue')

def animate(x):
    global t, total_time
    if t <= total_time:
        
         # Calculate new concentrations using the rate equations
        A.append(A[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt)
        B.append(B[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt)
        C.append(C[-1] + (2 * k1 * A[-1] * B[-1] - 2 * k2 * C[-1]) * dt)
        time.append(t)
        t += dt

    line_A.set_data(time, A)
    line_B.set_data(time, B)
    line_C.set_data(time, C)

animation = FuncAnimation(figure, animate, frames = 5, interval = 5)

# Set plot labels, legend, and title
plt.legend()
plt.title("Chemical Reactor")
plt.xlabel("Time (s)")
plt.ylabel("Mole/lt")
plt.show()