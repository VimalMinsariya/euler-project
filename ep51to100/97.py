import time
start = time.time()

def f(n):
    e = 0
    r = 1
    r34 = 7179869184
    m = 10**10
    while e+34 < n:
        e += 34
        r = (r*r34) % m
    result = (2**(n-e)*r) % m
    return result

print((28433*f(17957)+1)%(10**10))

print(time.time()-start)