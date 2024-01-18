'''

a = [[1, 2, 3], [4, 5, 6]]

i.e  1 2 3
     4 5 6
     
i.e 2x3 matrix (2 rows x 3 columns)
'''


m=[]
row = int(input("No. of Row: "))
col = int(input("No. of Column: "))
for i in range (row):
    r=[]
    for c in range (col):
        ele = int(input())
        r.append(ele)
    m.append(r)

print(m)


'''
OUTPUT:
No. of Row: 2
No. of Column: 2
1
2
3
4
[[1, 2], [3, 4]]
'''
