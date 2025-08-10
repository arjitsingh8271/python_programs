#QN1
a=int(input())
b=int(input())

t=a
a=b
b=t

print("a={}".format(a))
print("b={}".format(b))





#QN2
name=input()
print(name[::-1])





#QN3
data = input()

result = data.split()

print(result)






#QN4
def is_perfect_number(number):
    
    if number <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    
    return divisor_sum == number


num=int(input())

if is_perfect_number(num):
    print("{} is perfect".format(num))
else:
    print("{} is not perfect".format(num))







#QN5
def factorial(n):

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num=int(input())
result = factorial(num)
print(result)







#QN6
def fibonacci_series(limit):

    if limit < 0:
        return 0
    
    a, b = 0, 1
    print(a, end=" ")
    print(b, end=" ")

    for i in range (2,limit):
        c = a+b
        print(c, end=" ")
        a = b
        b = c
    

limit=int(input())
fibonacci_series(limit)