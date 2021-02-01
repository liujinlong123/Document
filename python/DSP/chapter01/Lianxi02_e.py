import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

min = -1
max = -min
sample = 48000

# y = sin(31 * pi * n / 5)
x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = np.sin(31 * pi * x_value / 5)

# plot
plt.plot(x_value, y_value, 'b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('y = sin(31 * pi * n / 5)')
plt.grid(True)

# 频率f = 31 / 10; 周期T = 10 / 31
x1 = 0
y1 = 0

x2 = 10 / 31
y2 = np.sin(2 * pi)

# 画竖线
plt.vlines(x=[x1, x2], ymin=-1.2, ymax=1.2, linestyles='dashed', color='r')

# 画圆点
plt.plot([x1], [y1], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x1, y1), xy=(
    x1, y1), xytext=(x1 + 0.01, y1))

plt.plot([x2], [y2], 'o', color='r')
plt.annotate(s='(%.5f, %.5f)' % (x2, y2), xy=(x2, y2), xytext=(x2 + 0.01, y2))

# show
plt.show()
