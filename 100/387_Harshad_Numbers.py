def prime_seive(n):
    num = {i:1 for i in range(2,n)}
    limit = int(n**(1/2))
    for k in range(2,limit+1):
        if num[k] == 1:
            for j in range(2*k,n,k):
                num[j] = 0
    return list(filter(lambda x: num[x]==1, num))

def isPrime(n):
    if n < N and n not in primes: return False
    if n >= N:
        for p in primes:
            if n%p == 0: return False
    return True

def digitsum(n):
    p, q = divmod(n,10)
    s = q
    while p > 0:
        p, q = divmod(p, 10)
        s += q
    return s

def isHarshad(n):
    return n%digitsum(n) == 0

def isTruncatable(n):
    while n>0:
        if not isHarshad(n): return False
        n //= 10
    return True

def truncatableHN(digit):
    if digit == 1:
        return [1,2,3,4,5,6,7,8,9]
    else:
        re = []
        li = truncatableHN(digit-1)
        for num in li:
            for n in range(10):
                new_num = 10*num + n
                if isHarshad(new_num): re.append(new_num)
    return re

def strongHN(digit):
    re = []
    l = truncatableHN(digit)
    for n in l:
        if isHarshad(n) and isPrime(n//digitsum(n)): re.append(n)
    return re

def strongTHP(digit):
    re = []
    l = strongHN(digit-1)
    for num in l:
        for n in [1,3,7,9]:
            new_num = 10*num + n
            if isPrime(new_num): re.append(new_num)
    return re

N = 10**7
limit = int(N**(1/2))
primes = prime_seive(N)
print('primes generated!')
a = []
for i in range(3,15):
    print(i, end=' ')
    a += strongTHP(i)
print('\r')
print(sum(a))
