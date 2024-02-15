#fibonaci series
def fibo(a,b,n):
    if n==0:
        return 0
    else:
        print(a)
        fibo(b,a+b,n-1)
a=0
b=1
n=int(input("Enter nth No. :"))
fibo(a,b,n)
