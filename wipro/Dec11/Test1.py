import sys

import numpy as np

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr = np.array(arr)

unique_elements = np.unique(arr)

print(unique_elements)