# Define a function to find the factorial of the number using recursion

def factorial(n):

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num=int(input())
result = factorial(num)
print(result)