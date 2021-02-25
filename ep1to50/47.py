import time
start = time.time()

def n_distinctfactor(n):
    n_factor = 0
    p = 3
    if n%2 == 0:
        while n%2 == 0:
            n /= 2
        n_factor += 1
    limit = int((n+1)**(1/2))
    while p < limit:
        if n%p == 0:
            while n%p == 0:
                n /= p
            n_factor += 1
            limit = int((n + 1) ** (1 / 2))
        if n_factor == 4 and n>1:
            break
        p += 2
    if n > 1:
        n_factor += 1
    return n_factor

target = 4
combo = 0
n = 2*3*5*7
while combo < target:
    if n_distinctfactor(n) == target:
        combo += 1
    else:
        combo = 0
    n += 1

print(n-4)

print('Elapsed Time:',time.time()-start)