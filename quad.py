import math
'''def isPrime(N):
    sqrt=int(math.sqrt(N)+1)
    if N==1:
        return False
    elif N==2 or N==3:
        return True
    else:
        for i in range(2,sqrt):
            if N%i==0:
                return False
        else:
            return True
def exactly3divisors(N):
    if N==1 or N==2 or N==3:
        return 0
    counter=0
    s=int(math.sqrt(N))
    for i in range(2,s+1):
        if isPrime(i):
            if i**2 in range(N+1):
                counter+=1
    return counter
print(exactly3divisors(1000000000))'''

'''def prime(n):
    counter=0
    s=int(math.sqrt(n)+1)
    if n==1:
        return 0
    else:
        for i in range(2,s):
            p=int(math.sqrt(i)+1)
            for j in range(2,p):
                if i%j==0:
                    break
            else:
                counter+=1
    return counter
print(prime(200))'''

'''    c=[]
    for ele in A:
        if ele not in c:
            c.append(ele)
    return c

A=[1,1,2,1,3,5,3,2,4,1,3,2,1]'''
'''def remove_duplicate(A,N):
    counter=0
    for i in range(0,):

    return A

A=[1,1,1,1,1,1,1,1,2,2,2]
print(remove_duplicate(A,7))'''

'''
A=[1,1,1,1,2,2,2,2,3,3,4,4,4,4,5]
def remove_duplicate(A,N):
    counter=1
    for i in range(1,N):
        if A[i-1]==A[i]:
            continue
        else:
            counter+=1
            A[counter-1]=A[i]
    A=A[0:counter]
    return (counter)

print(remove_duplicate(A,15))'''

'''arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
def rev(arr,n,k):
    for start_index in range(0,n,k):
        right=start_index+min(k-1,n-start_index-1)
        while start_index<right:
            temp=arr[start_index]
            arr[start_index]=arr[right]
            arr[right]=temp
            right=right-1
            start_index+=1
    return arr
print(rev(arr,17,6))'''

'''def broken(n):
    if n==1:
        return [[1]]
    l=[1]
    m=[]
    for i in broken(n-1):
        i=i+l
        m.append(i)
    for i in broken(n-1):
        for j in range(0,len(i)):
            p=i.copy()
            p[j]+=1
            if p not in m and p!=[n] and p[::-1] not in m:
                m.append(p)
    return m
print(broken(7))'''

'''def rev(A,D,N):
    T2=A[0]
    i=0
    while i<D:
        T1=A[N-D+i]
        A[N-D+i]=T2
        T2=A[N-2*D+i]
        A[N-2*D+i]=T1
        i+=1
    A[0]=T2
    return A 
A=[1,2,3,4,5,6,7,8]
print(rev(A,3,8))'''

'''def rot(A,D,N):
    T2=A[0]
    p=A[D]
    i=-1
    j=0
    if N%D!=0:
        while A[0]!=p :
            T1=A[i*D+j*N]
            A[i*D+j*N]=T2
            i-=1
            if i*D<(-j*N):
                j+=1
            T2=A[i*D+j*N]
            A[i*D+j*N]=T1
            i-=1
            T1=T2
            if i*D<(-j*N):
                j+=1
    else:
        for i in range(0,D):
            m=A[i+D]
            k=1
            while D*(k+1)<len(A):
                A[k*D+i]=A[D*(k+1)+i]
                k+=1
            A[D*k+i]=A[i]
            A[i]=m
    return A
A=[1,2,3,4,5,6,7,8,9,10,11]
print(rot(A,4,11))'''








        




