l1 = [i for i in range(1,6)]
print(l1)           # [1, 2, 3, 4, 5]


# List i.e factor of 10
li_fact = [i for i in l1 if(10%i==0)]
print(li_fact)      # [1, 2, 5, 10]


# Nester comprehesion list
nest_li = [[c for c in range(3)] for r in range(2)]
print(nest_li)      # [[0, 1, 2], [0, 1, 2]]


# In Python Shell
'''  
>>> nest_li = [[c for c in range(3)] for r in range(2)]
>>> nest_li
[[0, 1, 2], [0, 1, 2]]
'''


'''
# Prime no.
prime_li = [i for i in range(2, 11) if]
'''

# Matrix multiplication
mat1 = [[i for i in range(1, 3)] for j in range(1, 3)]
mat2 = [[i for i in range(1, 3)] for j in range(1, 3)]
print(mat1)
print(mat2)
mat3 = [[i for i in range(2)]]


















