a=input().split(' ')
b=input().split(' ')
c=b[::-1]
x=len(b)-b.count('0')
y=int(a[0])-int(c.index(b[int(a[1])-1]))
print(min(x,y))

#a=input().split()
#b=input().split()
#i=0
#j=0
#for m in a:
#    a[i]=int(m)
#    i+=1
#for n in b:
#    b[j]=int(n)
#    j+=1
#print(a,b)

#count=0
#for x in b:
#    if x>0 and x>=b[a[1]-1]:
#        count+=1
#print(count)