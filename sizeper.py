def subset(l,k):
    l1=[]
    if k==0:
        return [set()]
    else:
        for i in subset(l,k-1):
            for j in l:
                m=i.copy()
                m.add(j)
                if len(m)==k and m not in l1:
                    l1.append(m)
        return(l1)
l=[1,2,3,4,5]
k=3
print(subset(l,k))