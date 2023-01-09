def p_lvl2(l,e):
    p=[]
    if l==[]:
        p.append([e])
    else:
        for j in l:
            for i in range(0,len(j)+1):
                d=j.copy()
                d.insert(i,e)
                p=p+[d]
    return p

def permutation(l):
    if len(l)==0:
        return []
    else:
        e=l.pop()
        l1=permutation(l)
        return p_lvl2(l1,e)

l=[1,2,3]
print(permutation(l))