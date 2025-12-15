#simple code to display data in pie chart using matplotlib

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 20])

plt.plot(xpoints, ypoints)
plt.show()
