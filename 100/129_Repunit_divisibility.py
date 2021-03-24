def ord10(p,k):
    if p in ord_list:
        if k in ord_list[p]:
            return ord_list[p][k]
    else:
        ord_list[p] = dict()
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
    ord_list[p][k] = re
    return re

def factorization(n:int) -> dict:
    result = {}
    p = 2
    limit = (n+1)**(1/2)
    while p < limit:
        cnt = 0
        while p < limit:
            if n % p == 0:
                n = n // p
                cnt += 1
            else:
                break
        if cnt > 0:
            result[p] = cnt
        limit = (n+1)**(1/2)
        p += 1
    if n > 1:
        result[n] = 1
    return result

def gcd(m,n):
    if m < n:
        return gcd(n,m)
    else:
        if n == 0:
            return m
        else:
            return gcd(n,m%n)

ord_list = dict()

def A(n):
    fa = factorization(n)
    re = 1
    for p, k in fa.items():
        if p == 3: k += 2
        a = ord10(p,k)
        re = (re * a) // gcd(re,a)
    return re

n = 10**6
while True:
    check = n%2 != 0 and n%5 != 0
    if check:
        x = A(n)
        print(n,x)
        if x > 10**6:
            break
    n += 1

print(n)
