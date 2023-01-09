def new_subset(smol_subset,element):
    l=[]
    for i in smol_subset:
        l.append(i+[element])
    smol_subset=smol_subset+l
    return smol_subset

#old_subset=[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#new_element=4
#print(new_subset(old_subset,new_element))
def all_subset(l2):
    if l2==[]:
        return [[]]
    else:
        element=l2.pop()
        smol_subset=all_subset(l2)
        return new_subset(smol_subset,element)
l2=[1,2,3,4,5]
print(all_subset(l2))



    