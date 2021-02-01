import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

plt.figure(figsize=(8, 5), dpi=80)

# min ~ max
min = -10
max = -min

# x, y = cos(3 * pi * n)
# x_value = np.arange(min, max, step=0.001) * 3 * pi
x_value = np.linspace(min, max, 48000, endpoint=True)
y_value = np.cos(x_value * 3 * pi)

plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('cos(3 * pi * n)')
plt.grid(True)

# 频率f = 3 / 2; 周期T = 2 / 3
plt.vlines([0, 2/3], -1.2, 1.2, color="r", linestyles="dashed")

plt.show()
