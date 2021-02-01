import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

# cos0.01n*pi
x_value = np.arange(-300, 300)
y_value = np.cos(np.arange(-300, 300) * 0.01 * pi)

# matplotlib
plt.plot(x_value, y_value)
plt.grid(True)

# y = 0
zero_x_value = np.arange(-300, 300)
zero_y_value = np.arange(-300, 300) * 0
plt.plot(zero_x_value, zero_y_value, "r")

# 假设n=1 n_02=1 + T
print(np.cos(0.01 * 1 * pi))
print(np.cos(0.01 * (1 + 2 * 100) * pi))

# 周期T
print(2 * 100)

plt.show()
