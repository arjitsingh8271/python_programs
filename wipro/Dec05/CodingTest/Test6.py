# Define a function to display Fibonacci series up to the given limit.


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