def fibo(n):
    t1 = 0
    t2 = 1
    
    print(t1)
    print(t2)
    for i in range(1, n-1):
        f = t1 + t2
        t1 = t2
        t2 = f

        print(f)


num = int(input("Input: "))
fibo(num)
