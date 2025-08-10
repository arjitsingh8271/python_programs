def fib(n1,n2,n):
    if n1>n:
        return
    print(n1,end=" ")
    return fib(n2,n1+n2,n)
fib(0,1,34)
