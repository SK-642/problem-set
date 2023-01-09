def subsets(l):
    if len(l)==0:
        return [[]]
    final_subset=[]
    popped_ele=l.pop()
    print(popped_ele)
    for i in subsets(l):
        ns=i.copy()
        for j in range(0,len(ns)):
            ns.insert(j,popped_ele)
            print(ns)
            final_subset.append(ns)
    return final_subset
l={1,2,3}
print