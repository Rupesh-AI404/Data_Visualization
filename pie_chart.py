import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15, 10])
mylabels = ["Apples", "Bananas", "cherries", "Dates", "Elderberries"]

plt.pie(y, labels = mylabels)
plt.show()