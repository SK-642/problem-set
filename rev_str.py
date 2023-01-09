def rev(s):
    if len(s)>1:
        p=s[-1]
        return p+rev(s[:-1])
    else:
        return s
s=input()
print(rev(s)==s)
