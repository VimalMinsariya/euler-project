import time
start = time.time()

def sq(n:int) -> int:
    result = 1
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
            if p == 2:
                result *= p**(cnt//2)
            else:
                result *= p**((cnt+1)//2)
        limit = (n+1)**(1/2)
        if p == 2:
            p += 1
        else:
            p += 2
    if n > 2:
        result *= n
    return result

def F(N):
    sum = 0
    for n in range(1,N+1):
        sum += (N-n) // sq(n)
    sum += N
    return sum

N=10**6
print(F(N))

print(time.time()-start)