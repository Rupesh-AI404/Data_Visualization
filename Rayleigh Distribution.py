# Rayleigh distribution is used in signal processing.
#
# It has two parameters:
#
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
#
# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=2000), kind="kde")

plt.show()