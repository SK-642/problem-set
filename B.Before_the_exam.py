d,sumtime=map(int,input().split(' '))
m1=0
m2=0
for i in range(0,d):
    mintime,maxtime=map(int,input().split(' '))
    m1+=mintime
    m2+=maxtime
if m1>sumtime or m2<sumtime:
    print('no')
else:
    print('yes')

