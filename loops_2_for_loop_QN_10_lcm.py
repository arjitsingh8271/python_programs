"""

2|4, 3, 9, 6
2|2, 3, 9, 3
3|1, 3, 9, 3
3|1, 1, 3, 1
 |1, 1, 1, 1

LCM: 2X2X3X3 = 36

"""

n1 = int(input("Input: "))
n2 = int(input("Input: "))

if(n1>n2):
	temp=n1
else:
	term=n2

lcm=1

for i in range(2, term+2):
	if(n1%i==0 or n2%i==0):
		lcm *=i
	print(lcm)
print(lcm)
