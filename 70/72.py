import time
start = time.time()

def gcd(m,n):
    if m==n or n==0:
        return m
    elif m>n:
        r=m%n
        return gcd(n,r)
    else:
        return gcd(n,m)

def phi(n):
    result = 1
    m=n
    p=2
    up = m ** (1/2)
    while p <= up:
        e=0
        while p <= up:
            if m % p == 0:
                e += 1
                m = m//p
            else:
                break
        if e>0:
            result *= (p-1)*(p**(e-1))
            up = m ** (1 / 2)
        p += 1
    if m>1:
        result *= m-1
    return result

print(sum([phi(i) for i in range(1,10**6+1)])-1)
print(time.time()-start)
