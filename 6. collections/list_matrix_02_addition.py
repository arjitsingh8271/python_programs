m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]

m3 = []
for i in range (len(m1)):
    r=[]
    for j in range (len(m2)):
        ele = m1[i][j] + m2[i][j]
        r.append(ele)
    m3.append(r)

print(m1)
print(m2)
print(m3)


'''
OUTPUT:
[[1, 2], [3, 4]]
[[5, 6], [7, 8]]
[[6, 8], [10, 12]]
'''
