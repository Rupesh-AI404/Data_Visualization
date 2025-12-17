# Chi Square distribution is used as a basis to verify the hypothesis.
#
# It has two parameters:
#
# df - (degree of freedom).
#
# # size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=1, size=1000), kind="kde")

plt.show()