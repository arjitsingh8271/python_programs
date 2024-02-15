a = [3,8,12,13, 17]

#a.sort()

key = int(input())

l = 0
h = len(a)-1

while l <= h:
    mid = (l+h)//2
    
    if(a[mid] == key):
        print(mid)
    elif(a[mid] < key):
        l = mid+1
    else:
        h = mid-1