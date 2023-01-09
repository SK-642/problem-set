def pldr(s):
    if len(s)<=1:
        return True
    #elif len(s)==2:
        #return s[0]==s[1]
    elif len(s)>1:
        if s[0]==s[-1]:
            return pldr(s[1:-1])
        else:
            return False

s=input()
print(pldr(s))