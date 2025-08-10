n = int(input("Input: "))

is_prime = True

if(n==0 or n==1):
    is_prime = False
    
i = 2
while (i<=(n/2)):
    if(n%i==0):
        is_prime = False
    i = i+1

if(is_prime):
    print("Yes")
else:
    print("No")