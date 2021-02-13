import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# min ~ max
min = -20
max = -min
sample = 48000

# y = cos(πn / 2) - sin(πn / 8) + 3cos(πn / 4 + π / 3)
x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = np.cos(pi * x_value / 2) - np.sin(pi * x_value /
                                            8) + 3 * np.cos(pi * x_value / 4 + pi / 3)

# plot
plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('y = cos(πn / 2) - sin(πn / 8) + 3cos(πn / 4 + π / 3)')
plt.grid(True)

# y1 = cos(πn / 2) = 2πfn
# y2 = sin(πn / 8) = 2πfn
# y3 = 3cos(πn / 4 + π / 3) = 2πfn

# f1 = 1 / 4  T1 = 4
# f2 = 1 / 16 T2 = 16
# f3 = 1 / 8  T3 = 8

# T = 16;;

x1 = 0
y1 = np.cos(pi * x1 / 2) - np.sin(pi * x1 / 8) + \
    3 * np.cos(pi * x1 / 4 + pi / 3)

x2 = 16
y2 = np.cos(pi * x2 / 2) - np.sin(pi * x2 / 8) + \
    3 * np.cos(pi * x2 / 4 + pi / 3)

# Y Axis
plt.vlines(x=[x1, x2], ymin=-4.2, ymax=4.2, color='r', linestyles='dashed')

# point
plt.plot([x1], [y1], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x1, y1), xy=(x1, y1), xytext=(x1 + 0.1, y1))

plt.plot([x2], [y2], 'o', color='r')
plt.annotate(s='(%.1f, %.1f)' % (x2, y2), xy=(x2, y2), xytext=(x2 + 0.1, y2))

# show
plt.show()
