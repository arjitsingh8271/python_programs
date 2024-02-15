#Fibonacci Series
c=0
def fibonacci(n1,n2,l):
    print(n1,end=" ")
    global c
    c=c+1
    if(c==l):
        return 0
    return(fibonacci(n2,n1+n2,l))
        
(fibonacci(0,1,int(input("Enter nth Term :"))))
    
