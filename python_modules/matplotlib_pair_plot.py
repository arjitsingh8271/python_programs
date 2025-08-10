'''
Pair Plot:

A pair plot is a type of plot used to visualize pairwise 
relationships between variables in a dataset. It displays 
scatter plots for each pair of variables along with 
histograms on the diagonal for univariate distributions.
'''


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create pair plot
sns.pairplot(iris)
plt.show()