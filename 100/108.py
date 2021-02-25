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

ok = False
N = 1
while not ok:
    n_divisor = 1
    for i in factorization(N).values():
        n_divisor *= (2*i + 1)
    n_sol = (n_divisor + 1)//2
    if n_sol > 1000:
        ok = True
    N += 1

print(N-1)
