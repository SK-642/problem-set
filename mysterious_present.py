en,cw,ch=map(int,input().split(' '))
p=0
l=[]
el=[(0,0)]
for i in range(0,en):
    ew,eh=map(int,input().split(' '))
    if (ew>cw and eh>ch) and (ew,eh) not in el:
        p+=1
        el.append((ew,eh))
a=sorted(el)
for i in el[1:]:
    l.append(a.index(i))
if len(l)==0:
    print(0)
else:
    print(p)
    print(*l)
