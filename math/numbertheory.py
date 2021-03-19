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

def euler_phi(n):
    result = 1
    m = n
    p = 2
    up = int(m ** (1/2))
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
            up = int(m ** (1 / 2))
        p += 1
    if m>1:
        result *= m-1
    return result

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

def permutation(list,r):
    result = []
    if r == 0:
        return [[]]
    else:
        for i in range(len(list)):
            remLst = list[:i]+list[i+1:]
            for p in permutation(remLst,r-1):
                result.append([list[i]]+p)
        return result

def combination(list,r):
    result = []
    if len(list) == r and r > 0:
        return [list]
    elif r == 0:
        return [[]]
    else:
        first = list[0]
        remLst = list[1:]
        for p in combination(remLst,r-1):
                result.append([first]+p)
        for p in combination(remLst,r):
                result.append(p)
        return result

def coprime(n:int) -> list:
    test = [[i,j] for i in range(2,n) for j in range(1,i)]
    result = []
    for i in test:
        if (i[0]*i[1])%2 == 0:
            result.append(i)
        k = 2
        while i[0]*k < n:
            test.remove([i[0]*k,i[1]*k])
            k += 1
    return result

def gcd(m,n):
    if m < n:
        return gcd(n,m)
    else:
        if n == 0:
            return m
        else:
            return gcd(n,m%n)

def digit(n):
    set = {}
    while n > 0:
        r = n % 10
        if r not in set:
            set[r] = 1
        else:
            set[r] += 1
        n //= 10
    return set

# nthe_root(n) : length l below 0
def lys_root(m,n:int ,l:int) -> str:
    def difference(r, s, n):
        return (10 * r + s) ** n - (10 * r) ** n
    result = ''
    R,r,k = m,0,1
    while k < l + 1:
        p = 0
        test = 1
        while test > 0:
            test = R - difference(r,p,n)
            p += 1
        s = p - 2
        if k == 1:
            result += str(s) + '.'
        else:
            result += str(s)
        R = (R - difference(r,s,n))*(10**n)
        r = 10 * r + s
        k += 1
    return result

# 에라토스테네스 체
def esieve(n):
    li = [0,0] + [i for i in range(2,n+1)]
    sieve = []
    k = 0
    while k < n+1:
        if li[k] != 0:
            sieve.append(li[k])
            p = 2*k
            while p < n+1:
                li[p] = 0
                p += k
        k += 1
    return sieve
