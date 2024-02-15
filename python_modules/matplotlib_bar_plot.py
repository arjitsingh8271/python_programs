'''
Bar Plot:

A bar plot is a type of plot used to visualize categorical data by 
representing the values of different categories as bars. 
It is commonly used to compare the values of different categories 
or to show the distribution of a single categorical variable.
'''


import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()