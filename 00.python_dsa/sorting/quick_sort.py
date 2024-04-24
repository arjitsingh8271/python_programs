def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)



size = int(input("Enter Size: "))

list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
quick_sort(list1)
print(list1)
