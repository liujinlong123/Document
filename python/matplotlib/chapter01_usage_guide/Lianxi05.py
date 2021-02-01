import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
figure, axes = plt.subplots()

axes.plot(x, x, label='linear')
axes.plot(x, x**2, label="quadratic")
axes.plot(x, x**3, label="cubic")

axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title("Simple Plot")
axes.legend()

plt.show()
