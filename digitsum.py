def digit(n):
    '''
    xyz=x+y+z
    '''
    if n<10:
        return n
    else:
        x=n%10
        return (x+digit(n//10))
n=int(input())
print(digit(n))