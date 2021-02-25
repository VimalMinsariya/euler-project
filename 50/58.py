import time
start = time.time()

def isPrime(n):
    test_limit = int(n**(1/2))
    k=3
    result = True
    if n%2 == 0:
        return False
    while k <= test_limit:
        if n % k == 0:
            result = False
            break
        k += 2
    return result

n_dprime = 0
n_diagonal = 1
n=2
d=1
while n_dprime == 0 or n_dprime/n_diagonal >=0.1:
    for i in range(3):
        d += 2*(n-1)
        if isPrime(d):
            n_dprime += 1
    n_diagonal += 4
    d += 2*(n-1)
    n += 1

print(2*n-3)

print('Elapsed Time:',time.time()-start)