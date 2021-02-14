import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# min ~ max
min = 0
max = 12
sample = 48000


def f(t): return 3 * np.sin(100 * pi * t)


x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = f(x_value)

plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('x(t) = 3sin(100πt)')
plt.grid(True)


# Fs = 300Hz
def f(t): return 3 * np.sin(1 / 3 * pi * t)


x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = f(x_value)

plt.plot(x_value, y_value, color='r')


# Fs = 100Hz
def f(t): return 3 * np.sin(pi * t)


x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = f(x_value)

plt.plot(x_value, y_value, color='g')

# show
plt.show()
