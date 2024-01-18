n = int(input("Input: "))

for i in range(1,n):
	if (i*i <= n):
		if (i*i == n):
			print(f"Perfect square of {i}.")
			break
			
	else:
		print("Not a perfect square.")
		break


"""
OUTPUT: Input: 33
		Not a perfect square.

		
		Input: 25
		Perfect square of 5
"""