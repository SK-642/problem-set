#fib
#1.only recursion
import time
import sys
'''begin1 = time.time()
def fib(n):
    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursion
    return fib(n-1)+fib(n-2)

print(fib(35))
end1 =time.time()

print(f'R1={end1-begin1}')'''

#2.fib Using recursion and memoization
'''#defining a 1D array
begin2=time.time()
n = 50
dp=[-1]*(n+1)
def fib1(n,dp):
    #Base case remained same
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n]!=-1:
        return dp[n]
    dp[n] = fib1(n-1,dp)+fib1(n-2,dp)
    return dp[n]

print(fib1(n,dp))
end2 = time.time()
print(f'R2 = {end2-begin2}')'''

#Tabulation for fib
'''begin3=time.time()
def fib_tab(n):
    dp1=[-1]*(n+1)
    dp1[0] = 0
    dp1[1] = 1
    for i in range(2,n+1):
        dp1[i] = dp1[i-1] +dp1[i-2]
    return dp1[n]
print(fib_tab(50))
end3 = time.time()
print(f'R3 = {end3-begin3}')'''

#space optimization for fib
'''begin4 = time.time()
def fib_opt(n):
    prev1=1
    prev2=0
    for i in range(2,n+1):
        curr = prev1+prev2
        prev2=prev1
        prev1=curr
        #print(prev1)
    return prev1
print(fib_opt(50))
end4 =time.time()
print(f'R4 = {end4-begin4}')'''


#ways to climb n stairs
'''MOD = 1000007
def climb(N):
    #base case
    if N == 0:
        return 1
    elif N==1:
        return 1
    ways = climb(N-1) +climb(N-2) % MOD
    return ways
def climb2(N,i):
    if i == N:
        return 1
    elif i>N:
        return 0
    ways = climb2(N,i+1)+climb2(N,i+2) % MOD
    return ways

N=15
i=0
print(climb(N))
print(climb2(N,i))'''

#recursion + Memoization

'''def climb3(n,i,dp):
    #same base case
    if i==n:
        return 1
    elif i>n:
        return 0
    elif dp[i]!=-1:
        return dp[i]
    dp[i] = climb3(n,i+1,dp)+climb3(n,i+2,dp)
    return dp[i]%MOD

n=700
i=0
dp=[-1]*(n+1)
print(climb3(n,i,dp))'''

#Tabulation
'''def climb4(n,dp1):
    dp1[0]=1
    dp1[1]=1
    for i in range(2,n+1):
        dp1[i]=dp1[i-1]+dp1[i-2]
    return dp1[n]%MOD
dp1=[-1]*(n+1)
print(climb4(n,dp1))'''

#space optimization
'''def climb5(n):
    prev1=1
    prev2=1
    for i in range(2,n+1):
        curr=prev1+prev2
        prev2=prev1
        prev1=curr
    return prev1%MOD
print(climb5(n))'''

#min cost to climb n stairs
'''def solve(n,cost):
    if n==0:
        return cost[0]
    elif n==1:
        return cost[1]
    pay=cost[n]+min(solve(n-1,cost),solve(n-2,cost))
    return pay
def mincost(n,cost):
    ans=min(solve(n-1,cost),solve(n-2,cost))
    return ans
cost=[20,10,2,8,29,17,1,-6,5,12]
cost1=[10,15,20]
n=len(cost)
print(mincost(n,cost))'''

#rec+momo

'''def solve(n,cost,dp):
    if n==0:
        return cost[0]
    elif n==1:
        return cost[1]
    elif dp[n]!=-1:
        return dp[n]
    dp[n]=cost[n]+min(solve(n-1,cost,dp),solve(n-2,cost,dp))
    return dp[n]
def mincost(n,cost,dp):
    ans=min(solve(n-1,cost,dp),solve(n-2,cost,dp))
    return ans
cost=[20,10,2,8,29,17,1,-6,5,12]
cost1=[10,15,20]
n=len(cost)
dp=[-1]*(n+1)
print(mincost(n,cost,dp))'''

#Tabulation
'''def mincost2(n,cost):
    dp1=[-1]*(n)
    dp1[0]=cost[0]
    dp1[1]=cost[1]
    for i in range(2,n):
        dp1[i]=cost[i]+min(dp1[i-1],dp1[i-2])
        #print(dp1)
    return min(dp1[n-1],dp1[n-2])
print(mincost2(n,cost))'''

#space opti
'''def mincost3(n,cost):
    prev1=cost[1]
    prev2=cost[0]
    for i in range(2,n):
        curr=cost[i]+min(prev1,prev2)
        prev2=prev1
        prev1=curr
    return min(prev1,prev2)
print(mincost3(n,cost))'''

#minimum number of coins
#recursion only
'''def mincoin(deno,tar):
    #base case
    if tar==0:
        return 0
    elif tar == 1:
        return 1
    elif tar == 2:
        return 1
    elif tar == 3:
        return 2
    elif tar == 4:
        return 2
    elif tar == 5:
        return 1
    elif dp[tar]!=-1:
        return dp[tar]
    dp[tar] = min(mincoin(deno,tar-1),mincoin(deno,tar-2),mincoin(deno,tar-5))+1
    return dp[tar]
tar=150
dp=[-1]*(tar+1)
deno=[1,2,5]
print(mincoin(deno,tar))'''

num=[1,2,3,5]
x=21
'''def base(num,x):
    if x == 0:
        return 0
    elif x<0:
        return sys.maxsize
    mini=sys.maxsize
    for i in num:
        ans = base(num,x-i)
        if ans!=mini:
            mini=min(mini,1+ans)
    return mini
def mincoin(num,x):
    rec = base(num,x)
    if rec == sys.maxsize:
        return -1
    else:
        return rec
print(mincoin(num,x))'''

#rec+memo
'''def base(num,x,dp):
    if x == 0:
        return 0
    elif x<0:
        return sys.maxsize
    elif dp[x] != -1:
        return dp[x]
    mini=sys.maxsize
    for i in num:
        dp[x] = base(num,x-i,dp)+1
        if dp[x]!=mini:
            mini=min(mini,dp[x])
    return mini
def mincoin(num,x,dp):
    rec = base(num,x,dp)
    if rec == sys.maxsize:
        return -1
    else:
        return rec

num=[1,2,3,5,7,11]
x=157
dp=[-1]*(x+1)
print(mincoin(num,x,dp))'''

'''#tab'''
'''dp=[sys.maxsize]*(x+1)
dp[0] = 0
for i in range(x+1):
    for j in num:'''

#only by loops
'''def mincoin3(num,x):
    num=sorted(num)
    num=num[::-1]
    count = 0
    for i in num:
        if i > x:
            continue
        else:
            count+=x//i
            x=x%i
    return count

num = [1,2,3,5,6,7,9]
x=42
print(mincoin3(num,x))'''

#minimum moves of knight
'''def moves(A,B):
    count = 0
    quadrant_check = (A[0]-B[0],A[1]-B[1])
    local_square_moves={(A[0]-2,A[1]-2):4,(A[0]-1,A[1]-2):1,(A[0],A[1]-2):2,(A[0]+1,A[1]-2):1,(A[0]+2,A[1]-2):4,
                        (A[0]-2,A[1]-1):1,(A[0]-1,A[1]-1):2,(A[0],A[1]-1):3,(A[0]+1,A[1]-2):2,(A[0]+2,A[1]-2):1,
                        (A[0]-2,A[1]):2,(A[0]-1,A[1]):3,(A[0],A[1]):0,(A[0]+1,A[1]):3,(A[0]+2,A[1]):2,
                        (A[0]-2,A[1]+1):1,(A[0]-1,A[1]+1):2,(A[0],A[1]+1):3,(A[0]+1,A[1]+1):2,(A[0]+2,A[1]+1):1,
                        (A[0]-2,A[1]+2):4,(A[0]-1,A[1]+2):1,(A[0],A[1]+2):2,(A[0]+1,A[1]+2):1,(A[0]+2,A[1]+2):4}
    if B in local_square_moves.keys():
        return local_square_moves[B]
    prev1 = (200,200)
    prev2 = (200,200)
    while (prev1 and prev2) not in local_square_moves.keys():
        if quadrant_check[0]>=0 and quadrant_check[1]>=0:
            prev1 = (B[0]+2,B[1]+1)
            prev2 = (B[0]+1,B[1]+2)
            count+=1
            print(count)
        elif quadrant_check[0]>=0 and quadrant_check[1]<=0:
            prev1 = (B[0]+2,B[1]-1)
            prev2 = (B[0]+1,B[1]-2)
            count+=1
            print(count)
        elif quadrant_check[0]<=0 and quadrant_check[1]>=0:
            prev1 = (B[0]-2,B[1]+1)
            prev2 = (B[0]-1,B[1]+2)
            count+=1
            print(count)
        elif quadrant_check[0]<=0 and quadrant_check[1]<=0:
            prev1 = (B[0]-2,B[1]-1)
            prev2 = (B[0]-1,B[1]-2)
            count+=1
            print(prev1)
            #print(count)

    #if prev1 and prev2 in local_square_moves.keys():
    return count+min(local_square_moves[prev1], local_square_moves[prev2])
    #else:
        #count = 1+ min(moves(A,prev1),moves(A,prev2))
       # return count

A=(0,0)
B=(4,4)
print(moves(A,B))'''

#previous one did not work

#trying again
#Recursion


'''b=time.time()

A=(25,25)
B=(37,37)
N=39
def knight(A,B):
    #translating B to 1st quadrant
    B1=(abs(A[0]-B[0]),abs(A[1]-B[1]))
    #translation A to origin
    A=(0,0)
    #print(f'B1={B1}')
    local = {(0,0):0,(1,0):3,(2,0):2,(0,1):3,(1,1):2,(2,1):1,(0,2):2,(1,2):1,(2,2):4}
    if B1 in local.keys():
        #print(local[B1])
        return local[B1]
    else:
        B2=(abs(B1[0]-1),abs(B1[1]-2))
        B3=(abs(B1[0]-2),abs(B1[1]-1))
        #print(f'B2={B2}')
        #print(f'B3={B3}')
        moves = 1+min(knight(A,B2),knight(A,B3))
        #print(moves)
        return moves

print(knight(A,B))
e=time.time()
print(f'rec time={e-b}')


#Rec+Memoisation
b2=time.time()

dp=[]
for i in range(N+1):
    dp.append([])
    for j in range(N+1):
        dp[i].append(-1)

def knightMem(A,B,N,dp):
    #translating B to 1st quadrant
    B1=(abs(A[0]-B[0]),abs(A[1]-B[1]))
    #translation A to origin
    A=(0,0)
    #print(f'B1={B1}')
    #print(dp)
    local = {(0,0):0,(1,0):3,(2,0):2,(0,1):3,(1,1):2,(2,1):1,(0,2):2,(1,2):1,(2,2):4}
    if B1 in local.keys():
        #print(local[B1])
        return local[B1]
    elif dp[B[0]][B[1]]!=-1:
        return dp[B[0]][B[1]]
    else:
        B2=(abs(B1[0]-1),abs(B1[1]-2))
        B3=(abs(B1[0]-2),abs(B1[1]-1))
        #print(f'B2={B2}')
        #print(f'B3={B3}')
        dp[B[0]][B[1]] = 1+min(knightMem(A,B2,N,dp),knightMem(A,B3,N,dp))
        #print(dp[B[0]][B[1]])
        return dp[B[0]][B[1]]

print(knightMem(A,B,N,dp))
e2=time.time()
print(f'mem time={e2-b2}')'''

#working but TLE

#trying again anyhow
'''def knight(A,B,N):
    B1=(abs(A[0]-B[0]),abs(A[1]-B[1]))
    A=(0,0)
    print(B1)
    known = {(0,0):0,(1,0):3,(2,0):2,(0,1):3,(1,1):2,(2,1):1,(0,2):2,(1,2):1,(2,2):4,(0,3):3,(1,3):2,(2,3):3,(3,3):2,
            (3,2):3,(3,1):2,(3,0):3}
    count=0
    if B1 in known.keys():
        return known[B1]
    while B1[0]>1 and B1[1]>1 and B1 not in known.keys():
        if B1[0]<B1[1]:
            B1=(B1[0]-2,B1[1]-1)
            print(B1)
            count+=1
        else:
            B1=(B1[0]-1,B1[1]-2)
            print(B1)
            count+=1
    while B1[1]>2 and B1 not in known.keys():
        if B1[0]==0:
            B1=(1,B1[1]-2)
            print(B1)
            count+=1
        else:
            B1=(0,B1[1]-2)
            print(B1)
            count+=1
    while B1[0]>2 and B1 not in known.keys():
        if B1[1]==0:
            B1=(B1[0]-2,1)
            print(B1)
            count+=1
        else:
            B1=(B1[0]-2,0)
            print(B1)
            count+=1
    return known[B1]+count

A=(68,234)
B=(169,100)
N=393
print(knight(A,B,N))'''

#did not work

#solve by bfs
'''def minmoves(initial,final,N):
    dir=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    visited=set()
    dist=0
    q=[(initial,0)]
    while len(q)>0:
        pos,dist=q.pop(0)
        if pos[0]==final[0] and pos[1]==final[1]:
            return dist
        for d in dir:
            x=pos[0]+d[0]
            y=pos[1]+d[1]
            if (x,y) not in visited:
                visited.add((x,y))
                q.append(([x,y],dist+1))
initial=[5,6]
final=[23,34]
N=50
print(minmoves(initial,final,N))'''

#Max sum of non adjacent elements
'''def solve(nums,N):
    if N<0:
        return 0
    elif N==0:
        return nums[0]
    incl=solve(nums,N-2)+nums[N]
    excl=solve(nums,N-1)
    ans=max(incl,excl)
    return ans
    
def maxSum(nums,N):
    if N==0:
        return 0
    else:
        return solve(nums,N-1)

nums=[9,9,8,2,1]
N=5
print(maxSum(nums,N))'''

#rec+mem

'''def solveMem(nums,N,dp):
    if N<0:
        return 0
    elif N==0:
        return nums[0]
    elif dp[N]!=-1:
        return dp[N]

    incl=solve(nums,N-2)+nums[N]
    excl=solve(nums,N-1)
    dp[N]=max(incl,excl)
    return dp[N]
    
def maxSum1(nums,N):
    if N==0:
        return 0
    else:
        dp=[-1]*(N)
        return solveMem(nums,N-1,dp)
    
print(maxSum1(nums,N))'''

#tabulation
'''def solveTab(nums,N):
    dp=[-1]*N
    dp[0]=nums[0]
    for i in range(1,N):
        incl=dp[i-2]+nums[i]
        excl=dp[i-1]
        dp[i]=max(incl,excl)
    return dp[N-1]
        

def maxSum2(nums,N):
    if N==0:
        return 0
    else:
        return solveTab(nums,N)
print(maxSum2(nums,N))'''

#space opti
'''def maxSum3(nums,N):
    prev1=nums[0]
    prev2=0
    for i in range(1,N):
        incl = prev2 + nums[i]
        excl = prev1
        ans=max(incl,excl)
        prev2=prev1
        prev1=ans
    return prev1
print(maxSum3(nums,N))'''

#leetcode problem 122(buying or selling of stocks)
'''def maxProfit(price):
    N=len(price)
    buy=0
    sell=0
    profit=0
    for i in range(1,N):
        if price[i]<=price[i-1]:
            buy=i
        else:
            sell=i
            profit+=(price[sell]-price[buy])
            buy=i
    return profit
price1=[7,1,5,3,6,4]
price2=[1,2,3,4,5]
price3=[7,6,5,4,3]
price4=[7,1,6,9,5,7]
print(maxProfit(price4))'''

#no theft in adjacent houses in circular arrangement

'''def solve(l,N):
    prev1=l[0]
    prev2=0
    for i in range(N):
        incl=prev2+l[i]
        excl=prev1
        prev2=prev1
        prev1=max(incl,excl)
    return prev1

def theft(A):
    N=len(A)
    l1=A[:N-1]
    l2=A[1:]
    if N==1:
        return A[0]
    return max(solve(l1,N-1),solve(l2,N-1))

A=[3,2,8,5,12,21,5,2,4,9,16]
print(theft(A))'''

#cut into segments

'''def solve(n,x,y,z):
    if n==0:
        return 0
    elif n<0:
        return (-sys.maxsize)
    a=solve(n-x,x,y,z)+1
    b=solve(n-y,x,y,z)+1
    c=solve(n-z,x,y,z)+1
    return(max(a,b,c))
def cut(n,x,y,z):
    ans=solve(n,x,y,z)
    if ans<=0:
        return 0
    else:
        return ans

n=4
x=2
y=1
z=1
print(cut(n,x,y,z))'''

#Tabulation

'''def maximizeTheCuts(n,x,y,z):
    dp=[-100000]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        if (i-x)>=0:
            dp[i]=max(dp[i],(dp[i-x]+1))
        if (i-y)>=0:
            dp[i]=max(dp[i],(dp[i-y]+1))
        if (i-z)>=0:
            dp[i]=max(dp[i],(dp[i-z]+1))
        print (dp)
    if dp[n]<0:
        return 0
    else:
        return dp[n]
print (maximizeTheCuts(n,x,y,z))'''

#count derangements
#recursion
'''def solve(N):
    if N==1:
        return 0
    elif N==2:
        return 1
    return (N-1)*(solve(N-2)+solve(N-1))

def cout(N):
    if N==0:
        return 0
    ans= solve(N)
    return ans

N=5
print(cout(N))'''

#Memoization
'''def solveMem(N,dp):
    if N==1:
        return 0
    elif N==2:
        return 1
    elif dp[N] !=-1:
        return dp[N]
    dp[N] = (N-1)*(solveMem(N-2,dp)+solveMem(N-1,dp))
    return dp[N]

def cout1(N):
    if N==0:
        return 0
    dp=[-1]*(N+1)
    ans= solveMem(N,dp)
    return ans
print(cout1(N))'''

#Tabulation

'''def solveTab(N):
    dp=[-1]*(N)
    dp[0]=0
    dp[1]=1
    for i in range(2,N):
        dp[i] = i*(dp[i-2]+dp[i-1])
    return dp[N-1]

def cout2(N):
    if N==0:
        return 0
    elif N==1:
        return 0
    ans = solveTab(N)
    return ans
print(cout2(N))'''

#space optimization
'''def cout3(N):
    prev2=0
    prev1=1
    for i in range(2,N):
        curr=(i-1)*(prev1+prev2)
        prev2=prev1
        prev1=curr
    return prev1

print(cout(N))'''

#2D DP
#Max value in limited weight (Knapsack 0-1)

'''def solve(W,Wt,val,index):
    collection=0
    if index==0:
        if Wt[0]<=W:
            return val[0]
        else:
            return 0
    else:
        incl=0
        if Wt[index]<=W:
            incl=val[index]+solve(W-Wt[index],Wt,val,index-1)
        excl=solve(W,Wt,val,index-1)
        collection += max(incl,excl)
    return collection

def maxVal(W,Wt,val):
    if len(Wt)==0:
        return 0
    index=len(Wt)-1
    return solve(W,Wt,val,index)

W=78
Wt=[6,5,1,5,6,5,9]
val=[5,3,4,9,6,1,1]
print(maxVal(W,Wt,val))'''

#Memoization

'''def solveMem(W,Wt,val,index,dp):
    if index==0:
        if Wt[0]<=W:
            return val[0]
        else:
            return 0
    elif W<=0:
        return 0
    elif dp[index][W]!=-1:
        return dp[index][W]
    else:
        incl=0
        if Wt[index]<=W:
            incl=val[index]+solveMem(W-Wt[index],Wt,val,index-1,dp)
        excl=solveMem(W,Wt,val,index-1,dp)
        dp[index][W] = max(incl,excl)
    return dp[index][W]

def maxVal1(W,Wt,val):
    if len(Wt)==0:
        return 0
    index=len(Wt)-1
    dp=[]
    for i in range(index+1):
        dp.append([])
        for j in range(W+1):
            dp[i].append(-1)
    #print(dp)
    return solveMem(W,Wt,val,index,dp)

print(maxVal1(W,Wt,val))'''

#Tabulation

'''def solveTab(W,Wt,val,index):
    dp=[]
    for i in range(index+1):
        dp.append([])
        for j in range(W+1):
            dp[i].append(0)
    if Wt[0]<=W:
        dp[0][0]=val[0]
    else:
        dp[0][0]=0
    for i in range(1,index+1):
        for j in range(1,W+1):
            incl=0
            if Wt[i]<=W:
                incl=val[i]+dp[i][W-Wt[i]]
            excl=dp[i][W]
            dp[i][j] = max(incl,excl)
            print(dp)
    return dp[index][W]

def maxVal2(W,Wt,val):
    if len(Wt)==0:
        return 0
    index=len(Wt)-1
    #print(dp)
    return solveTab(W,Wt,val,index)

W=6
Wt=[1,4,2,5]
val=[5,3,5,6]
print(maxVal2(W,Wt,val))'''

#Combination sum IV problem

'''def solve(N,arr,tar):
    if tar==0:
        return 1
    elif tar<0:
        return 0
    count=0
    for i in arr:
        count+=solve(N,arr,tar-i)
    return count

def comb(N,arr,tar):
    if N==0:
        return 0
    return solve(N,arr,tar)

N=3
arr=[1,2,5]
tar=5
print(comb(N,arr,tar))'''

#Memoization

'''def solveMem(N,arr,tar,dp):
    if tar==0:
        return 1
    elif tar<0:
        return 0
    elif dp[tar]!=-1:
        return dp[tar]
    count=0
    for i in range(N):
        count+=solveMem(N,arr,tar-arr[i],dp)
    dp[tar]=count
    return dp[tar]

def comb1(N,arr,tar):
    if N==0:
        return 0
    dp=[-1]*(tar+1)
    return solveMem(N,arr,tar,dp)

print(comb1(N,arr,tar))'''

#Tabulation

'''def solveTab(N,arr,tar):
    dp=[0]*(tar+1)
    dp[0]=1
    for i in range(1,tar+1):
        for j in range(N):
            if i-arr[j]>=0:
                dp[i]+=dp[i-arr[j]]
    return dp[tar]

def comb2(N,arr,tar):
    if N==0:
        return 0
    return solveTab(N,arr,tar)

print(comb2(N,arr,tar))'''

#Get minimum squares

#rec+Memoization

'''def solve(arr,tar,dp):
    if tar==0:
        return 0
    elif tar<0:
        return sys.maxsize
    if dp[tar]!=-1:
        return dp[tar]

    mini=sys.maxsize
    for i in arr:
        res=solve(arr,tar-i,dp)+1
        print(f'res={res}')
        if res!=mini:
            mini=min(res,mini)
            dp[tar]=mini
            print(f'dp={dp}')
            print(f'mini={mini}')
    return dp[tar]

def minsq(tar):
    arr=[]
    i=1
    while i*i<=tar:
        arr.append(i*i)
        i+=1
    print(arr)
    dp=[-1]*(tar+1)
    ans=solve(arr,tar,dp)
    if ans==sys.maxsize:
        return -1
    return ans

tar=11
print(minsq(tar))'''

#Tabulation
        
'''def solveTab(arr,tar):
    dp=[sys.maxsize]*(tar+1)
    dp[0]=0
    for i in arr:
        for j in range(1,tar+1):
            if j-i>=0:
                dp[j]=min(dp[j],dp[j-i]+1)
    return dp[tar]

def minsq1(tar):
    arr=[]
    i=1
    while i*i<=tar:
        arr.append(i*i)
        i+=1
    ans=solveTab(arr,tar)
    if ans==sys.maxsize:
        return -1
    return ans

tar=56
print(minsq1(tar))'''


'''def tradecount(systemA, systemB):
    systemA=sorted(systemA)
    print(systemA)
    ans=[]
    count=0
    for i in systemB:
        while count<len(systemA) and i>=systemA[count]:
            count+=1
            print(count)
        ans.append(count)
    return ans

systemA=[2,7,4,8]
systemB=[6,10]
print(tradecount(systemA,systemB))'''

#good array

import math
'''def consum(N):
    if N==1:
        return 2
    l=[]
    i=1
    m=int(math.sqrt(N))
    while i<=m:
        if N%i == 0:
            if N//i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(N//i)
        i+=1
    if len(l)==2:
        return 4
    p=sorted(l)
    j=0
    count=0
    while j<len(p):
        if p[j]%2==0:
            if 2*p[j] in p:
                count+=1
        j+=1
    return len(p)-count


N=9
print(consum(N))'''

'''def countConsecutive(N):
    count = 0
    L = 1
    while( L * (L + 1) < 2 * N):
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            count += 1
        L += 1
    return (count+1)*2

N=18
print(countConsecutive(N))'''

'''#minimum of maximum sum of k subarray
            
def splitArray(arr,n, k):
    #self.arr = arr
    #self.k = k
    i , j = max(arr),sum(arr)+1
    while i < j:
        print(f'i={i}')
        print(f'j={j}')
        mid = i + (j-i) //2
        print(f'mid={mid}')
        su = 0
        cnt = 0
        for nu in arr:
            su += nu
            if su > mid:
                su = nu
                cnt += 1
        if cnt >= k:
            i = mid + 1
        else:
            j = mid    
    return i  

arr=[5,2,4,1]
n=len(arr)
k=4
print(splitArray(arr,n,k)) '''


def sort012(arr,n):
    i=0
    j=n-1
    while i<j:
        if arr[i]==2 and arr[j]==0:
            arr[i]=0
            arr[j]=2
            i+=1
            j-=1
            print(f'i={i},j={j}')
            print(f'arr={arr}')
        elif arr[i]==2 and arr[j]==1:
            arr[i]=1
            arr[j]=2
            j-=1
            print(f'j={j}')
            print(f'arr={arr}')
        elif arr[i]==1 and arr[j]==0:
            arr[i]=0
            arr[j]=1
            i+=1
            print(f'i={i}')
            print(f'arr={arr}')
        else:
            i+=1
            print(f'i={i}')
    return arr

arr=[0,2,1,2,0]
n=5
print(sort012(arr,n))
        


