from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=5, size=4000),
  "binomial": random.binomial(n=100, p=0.5, size=4000)
}

sns.displot(data, kind="kde")

plt.show()