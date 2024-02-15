'''
Matplotlib is a Python library used for data visualization. 
It provides a wide variety of plotting functions and styles 
to create different types of plots, such as scatter plots, 
line plots, bar plots, histograms, box plots, etc.


Scatter Plot:

A scatter plot is a type of plot used to visualize the relationship 
between two variables. Each point on the plot represents an observation 
in the data, with the x-axis and y-axis representing the two variables.

'''

import matplotlib.pyplot as plt

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()