import time

def generate_primes(N):
    primes = [2]
    p = 3
    while p < N+1:
        test = True
        limit = int(p**(1/2)) + 1
        for k in primes:
            if k < limit:
                if p % k == 0:
                    test = False
                    break
        if test:
            primes.append(p)
        p += 2
    return primes

def prime(primes,n):
    result = []
    for p in primes:
        if p < n+1:
            result.append(p)
    return result

start = time.time()
memo_e = dict()
memo_e_B = dict()
N = 20000
primes = generate_primes(N)
CUT = 1000000007

for p in primes:
    memo_e[p] = {0: 0}
    for i in range(1,N+1):
        memo_e[p][i] = i//p + memo_e[p][i//p]
    memo_e_B[p] = {0:0}
    for j in range(1,N+1):
        memo_e_B[p][j] = memo_e_B[p][j-1] + (j-1)*memo_e[p][j] - j*memo_e[p][j-1]

print("All deployed. Go!")
print(time.time()-start)

def power(p, e, CUT):
    result = 1
    q = e
    while q > 0:
        q, r = divmod(q,2)
        if r == 1:
            result = (result * p)%CUT
        p = (p*p)%CUT
    return result

def D(n):
    result = 1
    for p in prime(primes,n):
        result *= ((power(p, memo_e_B[p][n]+1, CUT) - 1) * (power(p-1,CUT-2,CUT)))%CUT
    return result%CUT

def S(n):
    result = 0
    for k in range(1,n+1):
        if k%1000 == 0:
            print(k)
        result += D(k)
    return result%CUT

print(S(N))

print(time.time()-start)