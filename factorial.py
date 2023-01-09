def factorial(n):
    '''
    n!=1x2x3x4....n
    '''
    if n==0:
        x=1
        return x
    if n>=1:
        y=n*factorial(n-1)
        return y
    #for x in range(2,n+1):
        #y=y*x
    #print(y)
n=int(input())
print(factorial(n))
