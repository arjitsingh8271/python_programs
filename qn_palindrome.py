'''
What is a Palindrome?
A palindrome is nothing but any number or a string which remains unaltered when reversed.

Example: 12321
Output: Yes, a Palindrome number

Example: RACECAR
Output: Yes, a Palindrome string
'''

# for number
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


'''
# for string or u can use a number also
var = input(("Enter a value: "))

# here we check var value is equal to reverce of var value
if(var == var[::-1]):
    print(f"The {var} is a palindrome")
else:
    print(f"The {var} is not a palindrome")
'''    