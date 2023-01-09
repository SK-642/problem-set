index=0
for a in [1,2,3,4,5]:
    x=3-a
    if x<0:
        x=(-1)*x
    b=input().split(' ')
    if '1' in b:
        c=2-b.index('1')
        if c<0:
            c=(-1)*c
        print(c+x)


    