'''
Histogram:

A histogram is a type of plot used to visualize the distribution 
of a continuous variable. It divides the range of values into 
intervals (bins) and counts the number of observations falling 
into each interval.
'''


import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6]
plt.hist(data, bins=5)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()