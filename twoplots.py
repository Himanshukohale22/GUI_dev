from matplotlib import pyplot as plt
import numpy as np

xPoints = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
y1Points = np.array([12, 14, 16, 18, 10, 12, 14, 16, 18, 120])
y2Points = np.array([12, 7, 6, 5, 4, 3, 2, 2, 1, 12])

plt.subplot(1, 2, 1) # row 1, col 2 index 1
plt.plot(xPoints, y1Points)
plt.title("My first plot!")
plt.xlabel('X-axis ')
plt.ylabel('Y-axis ')

plt.subplot(1, 2, 2) # index 2
plt.plot(xPoints, y2Points)
plt.title("My second plot!")
plt.xlabel('X-axis ')
plt.ylabel('Y-axis ')

plt.show()




