def lcm(n):
    m=6
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 6
    else:
        for j in range(4,n+1):
            i=1
            while (m*i)%j!=0:
                i+=1
            m=m*i
        return m
print(lcm(9))
