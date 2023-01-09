x=int(input())
for a in range(1,x+1):
    b=input()
    if len(b)<11:
        print(b)
    else:
        d=len(b)-2
        print(b[0]+str(d)+b[-1])

