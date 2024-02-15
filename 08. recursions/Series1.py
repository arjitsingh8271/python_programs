#1+1/2+1/3+1/4.....
def lcmSeries(n):
    if n==1:
        return 1;
    else:
        return 1/n + (lcmSeries(n-1))
print(lcmSeries(int(input("Enter nth Term :"))))
