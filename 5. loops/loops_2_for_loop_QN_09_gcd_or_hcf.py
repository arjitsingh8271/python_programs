"""
25)15(0
	0
   --
   15)25(1
   	  15
   	  --
   	  10)15(1
   	  	 10
   	  	 --
   	  	  5)10(2
   	  	  	10
   	  	  	--
   	  	  	00

GCD: 5
"""



n1 = int(input("Input: "))
n2 = int(input("Input: "))

rem = 0
temp = 0

while (n1 != 0 and n2 != 0):
	rem = n1%n2
	n1 = n2
	n2 = rem
	print(n1)

print(f"GCD: {n1}")



"""
OUTPUT: Input: 15
		Input: 25
		25
		15
		10
		5
		GCD: 5
"""