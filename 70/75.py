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


N = 150
cnt = 0
for i in range(2,int(N/2+1)):
    k = factorization(i)
    t = 1
    primes = []
    if len(k) == 2:
        for p,e in k.items():
            primes.append(p)
            t *= p
        primes = sorted(primes)
        if t == i :
            print(k,2*i)
            cnt += 1

print(cnt)