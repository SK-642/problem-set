#def sub(l,k):
    #if len(l)==0 or k==0:
        #return [set()]
    #l1=[]
    #s=set()
    #ele=l.pop()
    #for i in sub(l,k-1):
        #if len(i)==k-1:
            #l1.append(i)
            #print(l1)
    #    ns=i.copy()
    #    ns.add(ele)
    #    l1.append(ns)
    #return(l1)

l=[1,2,3,4]
k=3


def smol(l,e):
    l1=[]
    for i in l:
        j=i+[e]
        l1.append(j)
    l=l+l1
    return l

def subset(l,k):
    if len(l)==0 or k==0:
        return [[]]
    else:
        e=l.pop()
        l=subset(l,k)
        return smol(l,e)

print(subset(l,k))

#def subset(l,k):
#    l1=[]
#    if k==0:
#        return [set()]
#    else:
#        for i in subset(l,k-1):
#            for j in l:
#                m=i.copy()
#                m.add(j)
#                if len(m)==k and m not in l1:
#                    l1.append(m)
#        return(l1)
#print(subset(l,k))
         






