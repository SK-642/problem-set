def back(arr,N):
    arrange=sorted(arr)
    table=[]
    if N==0:
        return [True]*len(arr)
    else:
        for i in arr:
            
        '''for index,ele in enumerate(back(arr,N-1)):
                if N==arrange[index]:
                    table.append(True)
                elif True in back(arr,N-arrange[index]):
                    table.append(True)
                elif N-1<arrange[index]:
                    table.append(False) 
                else:
                    table.append(False)'''
        
        return table 

def track(arr,N):
    return True in back(arr,N)
arr=[1,10,7,4,6]
N=15
# print(back(arr,N))
print(track(arr,N))

