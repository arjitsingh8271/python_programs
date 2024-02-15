#Palindrome
def pal(num,s):
    if num:
        s=s*10+num%10
        return pal(num//10,s)
    return s
num=int(input("Enter Number :"))
s=0
p=pal(num,s)
print(p)
if p==num:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
p(121,0)
s=1
p(12,1)
s=12
p(1,12)
s=1
s=00'''

        
