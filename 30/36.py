import time

start = time.time()

def ispalindrome(n,base):
    reversed = 0
    k = n
    while k>0:
        reversed = base*reversed + k % base
        k = k // base
    return (n == reversed)

def makePalindromeBase2(n,oddlength):
    result = n
    if oddlength:
        n = n >> 1
    while n>0:
        result = (result << 1) + (n & 1)
        n = n >> 1
    return result

limit = 10**6
sum = 0
n = 1
p = makePalindromeBase2(n,True)
while p < limit:
    if ispalindrome(p,10):
        sum += p
    n += 1
    p = makePalindromeBase2(n,True)

n = 1
p = makePalindromeBase2(n,False)
while p < limit:
    if ispalindrome(p,10):
        sum += p
    n += 1
    p = makePalindromeBase2(n,False)

print(sum)

print(time.time()-start)