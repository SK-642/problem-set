x,y,z=list(map(int,input().split()))
if x==2:
    print('NO')
elif x>2:
    p=x//2
    if y in [p,p+1] and z in [p,p+1]:
        print('NO')
    else:
        print('YES')