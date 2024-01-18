# list items are ordered, changeable, and allow duplicate values.

li = [1, 'mango', 2.3, 'A']
print(li)                   # [1, 'mango', 2.3, 'A']
print(type(li))             # <class 'list'>
print(len(li))              # 4

print(li[2])                # 2.3

li[0] = 2
print(li)                   # [2, 'mango', 2.3, 'A']


li.insert(1, 'apple')       # in 1th position insert 'apple'

print(li)                   # [2, 'apple', 'mango', 2.3, 'A']                  
print(li[1:3])              # ['apple', 'mango']


li.append(1)
print(li)                   # [2, 'apple', 'mango', 2.3, 'A', 1]
print(li[:])                # [2, 'apple', 'mango', 2.3, 'A', 1]
li2 = ["linux", "mac"]
li.append(li2)
print(li)					# [2, 'apple', 'mango', 2.3, 'A', 1, ['linux', 'mac']]


li.reverse()				# it reverse the values
print(li)					# [['linux', 'mac'], 1, 'A', 2.3, 'mango', 'apple', 2]


a = [43, 22, 12, 4, 1]
a.sort()					# it arranged the values in accending order
print(a)					# [1, 4, 12, 22, 43]
