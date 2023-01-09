#LCM
'''def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
def LCM(n):
    lcm=1
    if n==1:
        return 1
    else:
        for i in range(2,n+1):
            lcm=(i*lcm)//gcd(lcm,i)
        return lcm

print(LCM(5))'''

#Absolute value
'''def abs(n):
    if n>=0:
        return n
    else:
        return -1*n

print(abs(-32))'''

'''#quadratic roots
def root(a,b,c):
    x1=(-b+((b**2-4*a*c)**0.5))/(2*a)
    x2=(-b-((b**2-4*a*c)**0.5))/(2*a)
    return x1,x2

print(root(1,1,1))'''

#digits in factorial
'''import math
def fac(n):
    counter=0
    factorial=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            factorial*=i
        while factorial>0:
            factorial=factorial//10
            counter+=1
        return counter
    counter=0
    if n<2:
        return 1 
    else:
        while n>1:
            counter+=math.log10(n)
            n-=1
        return int(counter)+1

print(fac(221))'''

#check prime
'''import time
start=time.time()
import math 
def prime(n):
    s=math.sqrt(n)
    if n==0 or n==1:
        return False
    elif n==2 or n==3:
        return True
    else:
        if n%6==1 or n%6==5:
            for i in range(2,int(s)+2):
                if n%i==0:
                    return False
            else:
                return True
        else:
            return False
end=time.time()
print(prime(7919))
print(end-start)

import time
start=time.time()
import math
def isPrime(N):
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
end=time.time()
print(isPrime(7919))
print(end-start)'''

#exactly 3 divisors(squares of prime)
'''import time
import math
start=time.time()
def exactly3d(N):
    counter=0
    s=int(math.sqrt(N)+1)
    if N==1:
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
end=time.time()

print(exactly3d(1000000))
print(end-start)


import math
import math
start=time.time()
def d3(N):
    def isPrime(N):
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
    if N==1 or N==2 or N==3:
        return 0
    counter=0
    s=int(math.sqrt(N))
    for i in range(2,s+1):
        if isPrime(i):
            if i**2 in range(N+1):
                counter+=1
    return counter
end=time.time()
print(d3(1000))
print(end-start)'''

#modulo_inverse

'''def modinv(a,m):
    for i in range(1,m):
        if (i*a)%m==1:
            return i
        else:
            continue
    else:
        return -1

print(modinv(10,17))''' 

#remove_duplicate
'''def remove_duplicate(a,n):
    for i in range(n-1):
        if a[i+1]!=a[i]:
            a.append(a[i])
    a.append(a[n-1])
    a=a[n:]
    return a

print(remove_duplicate([1,1,2,2,2,2,3,4,4,4,5,5,6,7,8,8,8],17))'''

'''def remove_duplicate(A, N):
    counter=1
    for i in range(1,N):
        if A[i-1]==A[i]:
            continue
        else:
            counter+=1
            A[counter-1]=A[i]
        #A=A[0:counter]
    return (counter)

print(remove_duplicate([1,1,2,2,2,2,3,4,4,4,5,5,6,7,8,8,8],17))'''

#reverse array in groups

'''def revarr(arr,N,K):
    for i in range(0,N,K):
        j=i+min(K-1,N-i-1)
        while i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
    return arr

print(revarr([1,2,3,4,5,6,7,8,9],9,5))'''

#rotate array
'''def rot(arr,N,D):
    for i in range(0,D):
        arr.append(arr[0])
        arr.pop(0)
    return arr

print(rot([1,2,3,4,5],5,2))'''

#count repeats among two
'''def majority(arr,n,x,y):
    countx=0
    county=0
    for i in arr:
        if i==x:
            countx+=1
        elif i==y:
            county+=1
    if countx==county:
        return min(x,y)
    elif countx>county:
        return x
    else:
        return y'''

#Transition point
'''def trans(arr,n):
    if 0 not in arr:
        return 0
    elif 1 not in arr:
        return -1
    else:
        for index,i in enumerate(arr):
            if i==1:
                return index'''

#Equilibrium point
'''def eq(A,N):
    if len(A)==1:
        return 1
    else:
        for i in range(1,N-1):
            if sum(A[:i])==sum(A[i+1:]):
                return i+1
        else:
            return -1
print(eq([1,2],2))'''

#leader
'''def lead(A,N):
    temp=0
    leader=[]
    for i in A[::-1]:
        if i>temp:
            temp=i
            leader.append(i)
    return leader[::-1]

print(lead([1,8,2,6,4,3,7,2],8))'''

#wave
'''def wave(arr,N):
    for i in range(1,N,2):
        temp=arr[i-1]
        arr[i-1]=arr[i]
        arr[i]=temp
    return arr 

print(wave([1,3,5,7,11,19,21,22],8))'''

#sub array=sum
'''def sub(arr,n,s):

    for i in range(n):
        start=arr[i]
        increment=i
        while start<s and increment<n-1:
            start=start+arr[increment+1]
            #print(start)
            increment+=1
            #print(increment)
        if start==s:
            return [i+1,increment+1]
    else:
        return [-1]
print(sub([180,170,4,6,8,18],5,180))'''


'''def subarr(arr,n,s):
    for i in range(n):
        left=s
        increment=i
        while left>0 and increment<n:
            left=left-arr[increment]
            increment+=1
        if left==0:
            return [i+1,increment]
    else:
        return [-1]
print(subarr([108,170,4,6,8,18],5,180))'''

'''def subarray(arr,n,s):
    for index,i in enumerate(arr):
        total=s
        total=total-i
        counter=1
        if total==0:
            return [index+1,index+1]
        else:
            while total>0 and (index+counter<n):
                total=total-arr[index+counter]
                counter+=1
            if total==0:
                return [index+1,index+counter]
            else:
                continue
    else:
        return [-1]
print(subarray([18,170,4,10,8,18],5,180))'''

'''def subArraySum(arr, n, s):
    index=0
    total=0
    for i in range(n):
        while total<s and index<n:
            total+=arr[index]
            index+=1
        if total==s:
            return [i+1,index]
        else:
            total=total-arr[i]
    else:
        return [-1]
print(subArraySum([7,3,7,10,5],5,28))'''

#repeats
'''def rep(arr,n):
    l=[]
    for index,ele in enumerate(arr):
        if ele in arr[index+1:]:
            l.append(index)
    if len(l)==0:
        return -1
    else:
        return min(l)+1


print(rep([1,8,3,2,5],5))'''

'''def repeat(arr,n):
    d={}
    l=[]
    count=0
    for i in arr:
        if i not in d:
            d[i]=count
            count+=1
        else:
            l.append(d[i])
            count+=1
    if len(l)==0:
        return -1
    else:
        return min(l)+1

print(repeat([1,5,2,3,4,6,2],7))'''

#smaller than x

'''def smol(arr,n,x):
    l=[]
    for i in arr:
        if i<x:
            l.append(i)
    if len(l)==0:
        return -1 
    else:
        return max(l)

print(smol([1,2,3,4,5],5,1))'''

#max sum for subarray 

'''def subsum(arr,n):
    d={}
    s=0
    for i in range(n):
        s=s+arr[i]
        d[i]=s
    for j in range(n-1):
        s=s-arr[j]
        d[n+j]=s
        print(d)
    return max(d.values())

print(subsum([-2,1,-3,4,-1,2,1,-5,4],9))
#subsum didnt work'''

#Kadane algorithm
'''def kadane(arr,n):
    max_sum=min(arr)
    for i in range(n):
        s=0
        increment=0
        while increment+i<n:
            s=s+arr[increment+i]
            increment+=1
            if s>max_sum:
                max_sum=s
    return max_sum

print(kadane([-1,-2,-3,-4,-5],5))'''

#smallest positive missing number

'''def missing(arr,n):
    m=max(arr)
    if m<=0:
        return 1 
    else:
        for i in range(1,m):
            if i in arr:
                arr.remove(i)
            else:
                return i
        else:
            return m+1

print(missing([1,2,3,4,5],5))

def miss(arr,n):
    l=set(sorted(arr))
    if 1 not in l:
        return 1 
    else:
        for i in range(1,len(l)+1):
            if i in l:
                l.remove(i)
            else:
                return i
        else:
            return i+1

print(miss([1,2,3,4,5],5))'''

#rearrange such that arr[i] becomes arr[arr[i]]

'''def arrange(arr,n):
    for i in range(n):
        arr.append(arr[arr[i]])
    #arr=arr[n:]
    return arr[n:]
print(arrange([4,0,2,1,3],5))'''

'''def re(arr,n):
    i=arr[0]
    m=0
    temp=arr[i]
    for p in arr:
        arr[m]=temp
        m+=1
        temp=p
    return arr
print(re([4,0,2,1,3],5))
        #temp2=temp1'''


#trapping rain water
'''def trap(arr,n):
    trapped=0
    for m in range(1,n-1):
        left=max(arr[:m])
        #print(f'left={left}')
        right=max(arr[m+1:])
        #print(f'right={right}')
        if arr[m]<min(left,right):
            trapped+=min(left,right)-arr[m]
            #print(f'trapped={trapped}')
    return trapped

print(trap([2,4,0,6,0,4,2],7))

def trapped(arr,n):
    trapped=0
    left_max=0
    right_max=0
    left=[]
    right=[]
    for i in arr:
        if i>left_max:
            left_max=i
        left.append(left_max)
    for j in arr[::-1]:
        if j>right_max:
            right_max=j
        right.append(right_max)
    print(left)
    print(right)
    for k in range(n):
        if arr[k]<min(left[k],right[n-k-1]):
            trapped+=min(left[k],right[n-k-1])-arr[k]
            print(trapped)
    return trapped


print(trapped([2,4,0,6,0,4,2],7))'''



#merge
'''def mer(arr1,arr2,n,m):
    i=0
    j=0
    brr1=arr1.copy()
    brr2=arr2.copy()
    temp1=brr1[i]
    temp2=brr2[j]
    for num in range(n):
        temp3=min(temp1,temp2)
        if temp3<temp1:
            arr1[num]=temp3
            j+=1
            if j<m:
                temp2=brr2[j]
            else:
                temp2=max(brr1+brr2)+1
        elif temp3<temp2:
            arr1[num]=temp3
            i+=1
            if i<n:
                temp1=brr1[i]
            else:
                temp1=max(brr1+brr2)+1
        else:
            arr1[num]=temp3
            i+=1
            if i<n:
                temp1=brr1[i]
            else:
                temp1=max(brr1+brr2)+1
    for num2 in range(m):
        temp3=min(temp1,temp2)
        #print(f'temp3={temp3}')
        if temp3<temp1:
            arr2[num2]=temp3
            j+=1
            if j<m:
                temp2=brr2[j]
            else:
                temp2=max(brr1+brr2)+1
        #print(f'temp2={temp2}')
        elif temp3<temp2:
            arr2[num2]=temp3
            i+=1
            if i<n:
                temp1=brr1[i]
            else:
                break
        else:
            arr2[num2]=temp3
            j+=1
            if j<m:
                temp2=brr2[j]
            else:
                temp2=max(brr1+brr2)+1
        #print(f'temp1={temp1}')
    return arr1,arr2
print(mer([10,12],[5,18,20],2,3))'''



#square root floor
'''def fsqrt(x):
    right=(x+1)//2
    left=0
    mean=(right+left)//2
    while right-left>2:
        if mean*mean==x:
            return int(mean)
        elif mean*mean<x:
            left=mean
            mean=(mean+right)//2
        else:
            right=mean
            mean=(mean+left)//2
    if right*right<=x:
        return right 
    elif mean*mean>x:
        return left
    else:
        return mean
print(fsqrt(676))'''

#position of k in an array 

'''def find(N,arr,K):
    left=0
    right=N-1
    mean=(left+right)//2
    if K>arr[N-1] or K<arr[0]:
        return -1
    elif arr[right]==K:
        return right
    elif arr[left]==K:
        return left
    else:
        while right-left>1:
            if arr[mean]==K:
                return mean
            elif arr[mean]<K:
                left=mean
                mean=(left+right)//2
            else:
                right=mean
                mean=(left+right)//2
        else:
            return -1

print(find(8,[2,3,5,6,12,14,17,18],18))'''

'''def bin(arr,n,k):
    l=0
    r=n-1
    mid=int(l+(r-l)/2)
    print (mid)
    while r-l>0 and l<n-2:
        mid=int(l+(r-l)/2)
        if arr[r]==k:
            return r
        elif arr[mid]==k:
            return mid
        elif arr[mid]>k:
            r=mid
            #mid=int(l+(r-l)/2)
            print (l,mid,r)
        else:
            l=mid
            #mid=int(l+(r-l)/2)
            print(l,mid,r)
    else:
        return -1

print(bin([1,3,5,6,7,8,10,11,13,14],10,14))'''

    
#peak element
'''def peak(arr,n):
    for index,ele in enumerate(arr[:n-2]):
        if ele>=arr[index+1]:
            return index
    else:
        return n-1

print(peak([2,3,4,5,4,3,6,2,7,6],10))'''

'''def peakele(arr,l,h,n):
    mid=int(l+(h-l)/2)
    if len(arr)==1:
        return 0
    elif arr[l]>=arr[l+1]:
        return l
    elif arr[h]>=arr[h-1]:
        return h
    if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
        return mid
    elif arr[mid]<arr[mid-1]:
        return peakele(arr,l,mid-1,n-2)
    elif arr[mid]<arr[mid+1]:
        return peakele(arr,mid+1,h,n)

print(peakele([2],0,0,1))'''

#find index in sorted and rotated array 

'''def Search(arr,n,k):
    ans=-1
    l=0
    h=n-1
    while h-l>=0:
        mid=l+((h-l)//2)
        print(l,mid,h)
        if arr[mid]==k:
            return mid
        elif arr[h]==k:
            return h
        elif arr[mid]<k and arr[h]>k:
            l=mid+1 
        elif arr[mid]<k and arr[h]<arr[mid]:
            l=mid+1
        elif arr[mid]>k and arr[l]>k and arr[mid]>arr[l]:
            l=mid+1
        elif arr[mid]<k and arr[l]<k and arr[mid]>arr[l]:
            l=mid+1
        else:
            h=mid-1       
    return ans
print(Search([286,287,313,393,414,425,441,452,454,471,486,
494,513,524,537,572,626,669,672,690,692,708,
713,765,815,821,839,871,879,885,899,943,946,
959,969,984,985,997,5,21,22,25,41,64,66,81,
102,119,123,156,165,167,171,187,258,272,277],57,258))'''

#merge sort
'''def mergesort(arr1,arr2):
    arr=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
            print(f'i={i}')
            print(arr)
        else:
            arr.append(arr2[j])
            j+=1
            print(f'j={j}')
            print(arr)
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    return arr
print(mergesort([1,5,9],[2,3,6]))'''

'''def mergesort(arr):
    if len(arr)>1:
        arr1=arr[:len(arr)//2]
        arr2=arr[len(arr)//2:]

        mergesort(arr1)
        mergesort(arr2)
        k=0
        i=0
        j=0
        print(f'arr1={arr1},arr2={arr2}')
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr[k]=arr1[i]
                i+=1
                #print(f'i={i}')
                print(f'arr={arr}')
            else:
                arr[k]=arr2[j]
                j+=1
                #print(f'j={j}')
                print(f'arr={arr}')
            k+=1
        while i<len(arr1):
            arr[k]=arr1[i]
            i+=1
            k+=1
            print(f'arr={arr}')
        while j<len(arr2):
            arr[k]=arr2[j]
            j+=1
            k+=1
            print(f'arr={arr}')
        return arr
print(mergesort([4,6,2,8]))'''

#QuickSort

'''def quicksort(arr,low,high):
    if low<high:
        piloc=partition(arr,low,high)
        quicksort(arr,low,piloc-1)
        quicksort(arr,piloc+1,high)
    return arr

def partition(arr,low,high):
    pivot=arr[high]
    i=-1
    for j in range(high):
        if arr[j]<pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    arr[high]=arr[i+1]
    arr[i+1]=pivot
    return i+1

print(partition([66,72,69,12,43,60,80,96,54,41,17,51],0,11))
print(quicksort([66,72,69,12,43,60,80,96,54,41,17,51],0,11))'''
            
