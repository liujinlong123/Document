import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

min = -10
max = -min

# cos(pi * 30 * n / 105)
x_value = np.linspace(min, max, num=48000, endpoint=True)
y_value = np.cos(pi * 30 * x_value / 105)

plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('cos(pi * 30 * n / 105)')
plt.grid(True)

# 频率f = 1 / 7; 周期T = 7
plt.vlines([0, 7], -1.2, 1.2, color="r", linestyles="dashed")

plt.show()
