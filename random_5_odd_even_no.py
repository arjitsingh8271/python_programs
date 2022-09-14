import random

even_no = 0
odd_no = 0

for i in range(1,6):
	a = random.randint(1,10)
	print(f"{i} Loop  {a}")
	
	if(a%2==0):
		print("\tis an even number.")
		even_no +=1
		
	else:
		print("\tis an odd number.")
		odd_no +=1

		

print(f"\nTotal even numbers is: {even_no}")
print(f"Total odd numbers is: {odd_no}\n")