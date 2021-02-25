import time
start = time.time()

def digit1(n,k):
    t = str(n)
    return int(t[k-1])

def digit2(n,k):
    p = k // n
    q = k % n
    if q == 0:
        p = p -1
        q = n
    N = 10**(n-1) + p
    return digit1(N,q)

def d(n):
    a = n
    n_digits = 1
    totaldigits = 9
    while totaldigits < a:
        a -= totaldigits
        n_digits += 1
        totaldigits = 9*(10**(n_digits-1))*n_digits
    return digit2(n_digits,a)

result=1
for i in range(7):
    result *= d(10**i)

print(result)

print('Elapsed Time:',time.time()-start)