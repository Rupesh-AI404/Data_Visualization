import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15, 10, 20, 43])
mylabels = ["Apples", "Bananas", "cherries", "Dates", "mango", "oranges", "strawberries"]

plt.pie(y, labels = mylabels)
plt.show()