def rot(arr,n):
    for i in range(0,n):
        arr.append(arr.pop(0))
    return arr

arr=[1,2,3,4,5,7,9]
print(rot(arr,6))