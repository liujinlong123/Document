import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label="Linear")
plt.plot(x, x**2, label="Quafratic")
plt.plot(x, x**3, label="Cubic")
plt.xlabel('x Label')
plt.ylabel('y Label')
plt.title('Simple Plot')
plt.legend()

plt.show()
