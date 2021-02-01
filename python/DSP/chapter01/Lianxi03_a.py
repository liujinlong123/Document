import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# min ~ max
min = -2
max = -min
sample = 48000

# y = 3cos(5t + pi / 6)
x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = np.cos(5 * x_value + pi / 6) * 3

# plot
plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('y = 3cos(5t + π / 6)')
plt.grid(True)

# 频率f = 5 / 2π; 周期T = 2π / 5
# (x1, y1) (x2, y2)
x1 = 0
y1 = np.cos(5 * 0 + pi / 6) * 3

x2 = 2 * pi / 5
y2 = np.cos(5 * 2 * pi / 5 + pi / 6) * 3

# 画竖线
plt.vlines(x=[x1, x2], ymin=-3.2, ymax=3.2, color='r', linestyles='dashed')

# 画圆点
plt.plot([x1], [y1], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x1, y1), xy=(x1, y1), xytext=(x1 + 0.1, y1))

plt.plot([x2], [y2], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x2, y2), xy=(x2, y2), xytext=(x2 + 0.1, y2))

# show
plt.show()
