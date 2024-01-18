def sum_dig(n):
    sum=0
    while(n!=0):
        sum +=(n%10)
        n//=10
    print(sum)

num = int(input("Input: "))
sum_dig(num)
