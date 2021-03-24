def ord10(p,k):
    q,r = divmod(10, p**k)
    n = 1
    li = p**(k-1)*(p-1)
    while r != 1 and n <= li//2:
        q,r = divmod(r*10, p**k)
        n += 1
    if r != 1:
        re = li
    else:
        re = n
    return re

def isPrime(n):
    result = True
    limit = (n+1)**(1/2)
    if n % 2 == 0:
        result = False
    else:
        k = 3
        while k < limit:
            if n % k == 0:
                result = False
                break
            k += 2
    return result

k = 0
s = 0
a = ord10(3,3)
N = 10**9
if N % a == 0:
    k += 1
    s += 3
p = 7
while k < 40:
    if isPrime(p):
        a = ord10(p,1)
        if N % a == 0:
            k += 1
            s += p
            print(k, p)
    p += 2

print(s)
