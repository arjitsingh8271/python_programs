#palindrome String
def pal(s):
    l=list(s)
    if len(s):
        if s[0].upper()!=s[-1].upper():
            return False
        return pal(s[1:-1])
    return True
s=input("Enter String :")
print(pal(s))
        
            
