n,k,t=map(int,input().split(' '))
p=n*k*t//100
q=0
l=[0]*n
for i in range(0,n):
    if p-q>=k:
        l[i]=k
        q+=k
    elif 0<p-q<k:
        l[i]=p-q
        q+=(p-q)
    else:
        l[i]=0
print(*l)