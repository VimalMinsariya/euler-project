import math

def prime_seive(n):
    num = {i:0 for i in range(2,n)}
    limit = int(n**(1/2))
    for k in range(2,limit+1):
        if num[k] == 0:
            for j in range(2*k,n,k):
                num[j] = 1
    return list(filter(lambda x: num[x]==0, num))

N =10**8
primes = prime_seive(N)
l = len(primes)
tail = l-1
cnt = 0
for start in range(l):
    if tail < start : break
    h = primes[start]
    while h*primes[tail] >= N:
        tail -= 1
    cnt += tail - start + 1

print(cnt)
