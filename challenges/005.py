'''
005
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as 
The answer is [answer].
'''

print("Enter three numbers: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
answer = (num1 + num2) * num3
print("The answer is", answer)
#print("The answer is", (int(num1) + int(num2)) * int(num3))