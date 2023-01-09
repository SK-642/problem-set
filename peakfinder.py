def peak(arr):
    peaks=[]
    for index,ele in enumerate(arr[1:-1]):
        if arr[0]>=arr[1]:
            peaks.append(arr[0])
        elif ele>=arr[index-1] and ele>=arr[index+1]:
            peaks.append(ele)
        elif arr[-1]>=arr[-2]:
            peaks.append(arr[-1])
    return peaks
arr=[3,5,2,1,7,5,9,7,4,2,0,5]
print(peak(arr))
       
