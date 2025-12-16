# Exponential distribution is used for describing time till next event e.g. failure/success etc.
#
# It has two parameters:
#
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#
# size - The shape of the returned array.


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.exponential(size=1000), kind="kde")

plt.show()