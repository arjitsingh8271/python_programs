def rev(n):
    rev = 0
    while(n!=0):
        rev = (rev*10) + (n%10)
        n//=10
    print(rev)

num = int(input("Input: "))
rev(num)