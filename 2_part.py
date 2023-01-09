import copy
'''def two_part(l):
    l1=[]
    if len(l)==0:
        return [set()]
    for index,ele in enumerate(l):
        dissect=[set()]
        l2=l.copy()
        l2.pop(index)
        s=set(l2)
        dissect[0].add(ele)
        dissect.append(s)
        l1.append(dissect)'''
    


def part(s):
    l=list(s)
    part_list=[]
    if len(s)==1:
        return [[s]]
    else:
        for index,ele in enumerate(l):
            first_part=set()
            second_part=set()
            l1=l.copy()
            e=l1.pop(index)
            if ele not in l1:
                first_part.add(ele)
                second_part.update(l1)
                if [second_part,first_part] not in part_list:
                    part_list.append([first_part,second_part])
    counter=0
    while len(part_list[-1][0])<(len(l)/2)-0.5:
        sub_list=[]
        for j in range(counter,len(part_list)):
            for i in part_list[j][1]:
                l3=copy.deepcopy(part_list[j])
                l3[0].add(i)
                l3[1].remove(i)
                if l3 not in sub_list and l3[::-1] not in sub_list:
                    sub_list.append(l3)
        counter+=len(part_list)
        part_list=part_list+sub_list
    return part_list


def k_part(l,k):
    #part_n=[]
    if k<2:
        return [set(l)]
    elif k==2:
        return part(l)
        '''part_list=part(l)
        counter=0
        while len(part_list[-1][0])<(len(l)/2)-0.5:
            sub_list=[]
            for j in range(counter,len(part_list)):
                for i in part_list[j][1]:
                    l3=copy.deepcopy(part_list[j])
                    l3[0].add(i)
                    l3[1].remove(i)
                    if l3 not in sub_list and l3[::-1] not in sub_list:
                        sub_list.append(l3)
            counter+=len(part_list)
            part_list=part_list+sub_list
        return part_list'''
    else:
        final_list=[]
        for i in k_part(l,k-1):
            for j in range(0,len(i)):
                if len(i[j])==1:
                    continue
                else:
                    m=i.copy()
                    ele=m.pop(j)
                    #print(ele)
                    for _ in part(ele):
                        n=m+_
                    if n not in final_list:
                        final_list.append(n)

        return final_list
        '''for i in k_part(l,k-1):
            for j in range(0,len(i)):
                sub=set()
                h=part(i[j])
                for _ in h[j]:
                    sub.update(_)
            #    p=part(i[j])
            final_list.append(sub)
        return final_list'''
        '''part_list=part(l)
        final_list=[]
        for i in part_list:
            p=[]
            p.append(i[0])
            q=k_part(list(i[1]),k-1)
            for m in q[0]:
                p.append(m)
            if p not in final_list:
                final_list.append(p)
        return final_list'''

l=[1,2,3]
print(k_part(l,3))


