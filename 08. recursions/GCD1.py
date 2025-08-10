'''#GCD
def gcd(n1,n2,temp):
    print(n1,n2,temp,sep=',')
    if n1%temp==0 and n2%temp==0:
        return temp
    else:
        return gcd(n1,n2,temp-1)
n1=int(input("Enter Number :"))
n2=int(input("Enter Number :"))
if n1<=n2:
    temp=n1
else:
    temp=n2
print(gcd(n1,n2,temp))'''
#GCD
def gcd(n1,n2):
    if n2%n1:
        return gcd(n2%n1,n1)
    return n1
        
n1=int(input("Enter Number :"))
n2=int(input("Enter Number :"))
print(gcd(n1,n2))
'''
n2=10
n1=15
t=n2%n1=5
n2=5
n1=10
t=0
'''
'''
g(4,10)
t=4
g(4,10,3)
t=3
g(4,10,2)
t=2'''
