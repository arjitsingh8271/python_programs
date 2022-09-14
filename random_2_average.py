import random

sum = 0
for i in range(5):
    num = random.randint(1,100)
    print(num)
    sum += num

total = sum / 5
print(f"Average of Random Five no. is:{total}")
    
