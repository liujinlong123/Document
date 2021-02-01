import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

'''
x(n) = 2exp[j(n/6 - π)]

exp(jθ)  = cosθ + jsinθ
exp(-jθ) = cosθ - jsinθ

x(n) = 2cos(n/6 - π) + 2jsin(n/6 - π)
'''

# min ~ max
min = -2
max = -min
sample = 4

# x(n) = 2cos(n/6 - π) + 2jsin(n/6 - π)
x_value = np.linspace(min, max, num=(max - min) * sample, endpoint=True)
y_value = 2 * np.cos(x_value / 6 - pi) + 2j * np.sin(x_value / 6 - pi)

print(y_value)

# plot
# plt.plot([0,a[x].real],[0,a[x].imag],'ro-',label='python')
plt.plot(x_value, y_value, color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('x(n) = 2cos(n/6 - π) + 2jsin(n/6 - π)')
plt.grid(True)

plt.show()
