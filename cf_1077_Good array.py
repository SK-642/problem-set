N=int(input())
arr=list(map(int,input().split(' ')))
count=0
ans=[]
for i in range(N):
    ele=arr.pop(i)
    s=sum(arr)
    for j in arr:
        if s-j==j:
            count+=1
            ans.append(i+1)
    arr.insert(i,ele)
if count==0:
    print(count)
else:
    print(count)
    print(*ans)