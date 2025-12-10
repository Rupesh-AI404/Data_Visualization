import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
y = np.random.normal(160, 10, 250)
z = np.random.normal(180, 10, 250)


plt.hist(x)
plt.hist(y)
plt.hist(z)
plt.show()