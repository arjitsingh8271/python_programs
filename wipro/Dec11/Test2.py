import sys
import numpy as np

n = int(input())

print()
elements = [int(input()) for _ in range(n)]

arr = np.array(elements)

sum_elements = np.sum(arr)
product_elements = np.prod(arr)
min_element = np.min(arr)
max_element = np.max(arr)
sorted_array = np.sort(arr)

print(f"Original array: {arr}")
print(f"Sum of array elements: {sum_elements}")
print(f"Product of array elements: {product_elements}")
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")
print(f"Sorted array: {sorted_array}")

