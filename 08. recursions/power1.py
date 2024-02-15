#power
def power(x,n):
    if n:
        return x*power(x,n-1)
    return 1
        

    
x=int(input("X(number) :"))
n=int(input("N(power) :"))

print(power(x,n))
'''x=2  n=3
2*p(2,2)
2*p(2,1)
2*p(2,0)
1'''
