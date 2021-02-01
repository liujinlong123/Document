import matplotlib.pyplot as plt


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.ylabel('y label')
# plt.xlabel('x label')
# plt.axis([0, 6, 0, 20])
# plt.show()

figure, (axes1, axes2) = plt.subplots(1, 2)
axes1.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
axes2.plot([0, 6, 0, 20])
plt.show()
