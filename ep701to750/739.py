from time import thread_time

def P(n,r):
    re, t = 1, 0
    if r < 0: return 0
    while t < r :
        re *= (n-t)
        t += 1
    return re

def C(n,r):
    if n-r < r: r = n-r
    if r < 0 : return 0
    return P(n,r)//P(r,r)

def catalan(n):
    return C(2*n,n)//(n+1)

def fi(n):
    if n in [0,1]: return 1
    f0 , f1 = 1, 1
    k = 2
    while k < n+1:
        fi = f1 + f0
        fi = fi%1000000007
        f1, f0 = fi, f1
        k += 1
    print(thread_time())
    return (fi,f0)

def fi2(n):
    L = 1000000007
    if n in [0,1]: return 1
    if n%2 == 0:
        m = n//2
        a,b = fi(m)
        return (a**2 + b**2)%L
    else:
        m = n//2
        a,b = fi(m)
        return (a**2+2*a*b)%L

def f_next(nu,de):
    next_nu, next_de = [], [1]
    L = 1000000007
    k = nu[0] // de[0]
    for i in range(1,len(de)):
        if i < len(nu):
            t = nu[i]-k*de[i]
            next_nu.append(t%L)
        else:
            t = -k*de[i]
            next_nu.append(t%L)
        next_de.append((de[i]-de[i-1])%L)
    next_de.append(-de[-1])
    return (next_nu, next_de)

def lucas(n):
    if n==0: return 1
    if n == 1: return 3
    l0 , l1 = 1, 3
    k = 2
    while k < n+1:
        li = l1 + l0
        li = li%1000000007
        l1, l0 = li, l1
        k += 1
    print(thread_time())
    return li

print(lucas(10000000))