from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}

sns.displot(data, kind="kde")

plt.show()