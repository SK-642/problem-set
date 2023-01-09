d={}
for i in range(0,int(input())):
    name=input()
    if name in d.keys():
        d[name]+=1
        print(name+str(d[name]))
    else:
        d[name]=0
        print('OK')
