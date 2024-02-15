#1+1/2+1/3+1/4+......+1/n
def series(n):
    if n==1:
        return 1
    else:
        return series(n-1)+1/n
n=int(input("ENTER Nth value :"))
print(series(n))
'''
s(5)
s(4)+1/5
s(3)+1/4
s(2)+1/3
s(1)
'''
