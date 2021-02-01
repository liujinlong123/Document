import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100)
figure, (axes1, axes2) = plt.subplots(1, 2)
axes1.plot(data1, data2)
axes2.plot(data3, data4)
plt.show()
