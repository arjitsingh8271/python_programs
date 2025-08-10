'''
Line Plot:

A line plot is a type of plot used to visualize the trend or 
relationship between two variables over a continuous range. 
It is commonly used to display time series data or data with 
sequential observations.
'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()