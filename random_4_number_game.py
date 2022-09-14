import random

num = random.randint(1, 6)

for i in range(1,6):
    print(f"chance: {i}\n")
    b = int(input("Enter the number for guess: "))

    if (num == b):
        print("Your guess number is right\n")
        break
    
    elif (num>b):
        print("Number is to low\n")
        
    elif (num<b):
        print("Number is to high\n")
