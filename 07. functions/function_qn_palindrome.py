def pali(n):
    rev = 0
    temp = n
    while(n!=0):
        rev = (rev*10) + (n%10)
        n//=10

    if (temp == rev):
        print("Palindrome")
    else:
        print("Not Palindrome")


num = int(input("Input: "))
pali(num)
