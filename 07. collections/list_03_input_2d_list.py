def add(r1,c1):
    for i in range(r1):
        for j in range(c1):
            c[i][j]=mat1[i][j]+mat2[i][j]
    print(c)



r = int(input("No. of Rows: "))
c = int(input("No. of Columns: "))

li = []

for i in range(r):
	row=[]
	for j in range(c):
		ele = int(input())
		row.append(ele)
	li.append(row)

print(li)
add(r,c)


'''
OUTPUT: No. of Rows: 2
		No. of Columns: 4
		1
		2
		3
		4
		5
		6
		7
		8
		[[1, 2, 3, 4], [5, 6, 7, 8]]
'''
