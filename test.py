import matplotlib.pyplot as plt
import numpy as np

# Example list of values
data_list = [1, 3, 5, 2, 8, 4]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each element with a time delay
for i, value in enumerate(data_list):
    ax.plot(i, value, 'bo')  # 'bo' represents blue circles
    plt.pause(1)  # Adjust the time delay (in seconds)

# Show the final plot
plt.show()
