'''
Box Plot

A box plot (box-and-whisker plot) is a type of plot used to visualize 
the distribution and spread of data along with its median and quartiles. 
It provides a visual summary of the central tendency, dispersion, and 
skewness of the data.
'''


import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6]
plt.boxplot(data)
plt.xlabel('Values')
plt.ylabel('Distribution')
plt.title('Box Plot')
plt.show()