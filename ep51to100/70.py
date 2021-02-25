import time
start = time.time()

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

min = 3
for n in range(2,10**7):
    k = euler_phi(n)
    if digit(k) == digit(n):
        print(n)
        if min > n/k:
            min = n/k
            result = n

print(result,min)


print(time.time()-start)