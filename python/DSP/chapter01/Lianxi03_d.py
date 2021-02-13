import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# min ~ max
min = -100
max = -min
sample = 48000

# y = cos(n / 8)cos(πn / 8)
x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
# y_value = np.cos(x_value / 8) * np.cos(pi * x_value / 8)

# y = cosAcosB = 0.5cos(A + B) + 0.5cos(A - B)
# 相加的倍数是最小公倍数
# y1 = cos(n / 8 + πn / 8) = cos((1 + π)n / 8) = cos(2πfn)
# y2 = cos(n / 8 - πn / 8) = cos((1 - π)n / 8) = cos(2πfn)

# f1 = (1 + π) / 16π
# f2 = (1 - π) / 16π

# T1 = 16π / (1 + π)
# T2 = 16π / (1 - π)

# T = 256π^2 / (1 - π^2)
y_value = 0.5 * np.cos(x_value / 8 + pi * x_value / 8) + \
    0.5 * np.cos(x_value / 8 - pi * x_value / 8)

# plot
plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('y = cos(n / 8)cos(πn / 8)')
plt.grid(True)

# show
plt.show()
