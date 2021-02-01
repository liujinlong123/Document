import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100)
figure, axes = plt.subplots(1, 1)
axes.plot(data1, data2)
# axes.plot(data3, data4)
plt.show()
