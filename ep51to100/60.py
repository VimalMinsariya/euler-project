def sumOfDigit(n):
    s, q = 0, n
    while q > 0:
        q, r = divmod(q,10)
        s += r
    return s

def isPrime(n):
    limit = (n+1)**(1/2)
    if n == 1: return False
    if n == 2: return True
    if n%2 == 0: return False
    else:
        k = 3
        while k < limit:
            if n % k == 0: return False
            k += 2
    return True

def isPairPrime(p,q):
    a = int(str(p)+str(q))
    if sumOfDigit(a) % 3 == 0: return False
    b = int(str(q)+str(p))
    result = isPrime(a) and isPrime(b)
    return result

def isMember(u,q):
    for p in u:
        if not isPairPrime(p,q): return False
    return True

series = [[3]]
q = 7
test = True
while test:
    if isPrime(q):
        for u in series:
            if isMember(u,q):
                series.append(u+[q])
            if len(series[-1]) == 5:
                test = False
                break
        series.append([q])
    q += 2

print(series[-2], sum(series[-2]))