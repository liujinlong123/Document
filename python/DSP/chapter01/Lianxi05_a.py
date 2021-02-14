import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# min ~ max
min = 0
max = 30 / 1000
sample = 48000


def f(t): return 3 * np.sin(100 * pi * t)


# x(t) = 3sin(100πt)
x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = f(x_value)

# plot
plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('x(t) = 3sin(100πt)')
plt.grid(True)

# 100πt = 2πft
# f = 50  T = 20ms = 0.02

T = 1 / 50

x1 = 0
y1 = f(x1)

x2 = x1 + T
y2 = f(x2)

# Y Axis
plt.vlines(x=[x1, x2], ymin=-3.2, ymax=3.2, color='r', linestyles='dashed')

# point
plt.plot([x1], [y1], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x1, y1), xy=(x1, y1), xytext=(x1 + 0.001, y1))

plt.plot([x2], [y2], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x2, y2), xy=(x2, y2), xytext=(x2 + 0.001, y2))

# show
plt.show()
