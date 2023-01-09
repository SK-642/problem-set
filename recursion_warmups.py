def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)

def sum_of_digits(n):
    return 0 if n==0 else n%10 + sum_of_digits(n//10)

def reverse(st):
    return st if len(st)==1 else st[-1]+reverse(st[:-1])

def is_palindrome(st):
    return True if len(st)<2 else (st[0]==st[-1] and is_palindrome(st[1:-1]))

def is_subsequence(st1, st2):
    if len(st1)==0:
        return True
    index = st2.find(st1[0])
    if index == -1:
        return False
    else:
        return is_subsequence(st1[1:], st2[index:])

st=input()
print(is_palindrome(st))

