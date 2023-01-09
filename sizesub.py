def sub(l,k):
    l1=[]
    m=1
    j=0
    while len(l)>=k:
        for index,i in enumerate(l[:len(l)-k+1]):
            print(f'i={i}')
            if l[:k-1] not in l1:
                print(f'1st append={l[:k-1]}')
                l1.append(l[:k-1])
                print(f'2nd append={l[k-1+index]}')
                l1[index+j].append(l[k-1+index])
                print(f'l1 = {l1}')
        l.pop(m)
        print(f'l={l}')
        j=len(l1)
    return l1

def subset(l,k):
    l3=[]
    p=0
    for i in l:
        temp=sub(l[p:],k)
        print(f'temp={temp}')
        for j in temp:
            if j not in l3: 
                l3=l3+[j]
                print(f'l3={l3}')
        p+=1
    return(l3)
l=[1,2,3,4,5]
k=3
print(subset(l,k))

def subs(l,k):
    su=[[]]
    for i in range(len(l)+1):
        for j in range(i):
            su.append(l[j:i])
    return su
print(subs([1,2,3,4,5],3))
            



