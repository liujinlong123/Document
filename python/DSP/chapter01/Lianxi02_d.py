import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# range
min = -2.5
max = -min

# y = sin(3n)
x_value = np.linspace(min, max, num=48000, endpoint=True)
y_value = np.sin(3 * x_value)

# plot
plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('y = sin(3n)')
plt.grid(True)

# 频率f = 3 / (2pi)
plt.vlines(x=[0, 2 * pi / 3], ymin=-1.2, ymax=1.2,
           color='r', linestyles="dashed")

# (0, 0); (2pi / 3, sin(2pi))
plt.plot([0], [0], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' %
             (0, 0), xy=(0, np.sin(0)), xytext=(0.1, 0))

x2 = 2 * pi / 3
y2 = np.sin(2 * pi)
plt.plot([x2], [y2], 'o', color='r')
plt.annotate(s='(%.5f, %.5f)' % (x2, y2), xy=(x2, y2), xytext=(x2 + 0.1, y2))

# show
plt.show()
