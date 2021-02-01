import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0., 5., 0.2)

plt.plot(time, time, 'r--', time, time**2, 'bs', time, time**3, 'g^')
plt.show()
