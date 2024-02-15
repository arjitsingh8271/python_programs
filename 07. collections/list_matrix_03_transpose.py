m1 = [[1, 2, 3, 4], [5, 6, 7, 8]]

m2 = []
for i in range(4):
    r=[]
    for j in range(2):
        r.append(m1[j][i])
    m2.append(r)

print(m1)
print(m2)


'''
OUTPUT:
[[1, 2, 3, 4], [5, 6, 7, 8]]
[[1, 5], [2, 6], [3, 7], [4, 8]]
'''
