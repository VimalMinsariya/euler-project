def chain(n):
    k=0
    while(n>1):
        if n % 2 == 0:
            n = n/2
            k += 1
        else:
            n = 3*n + 1
            k += 1
    return k

import time
start = time.time()

lc=0
t=1
while(t<1000000):
    a = chain(t)
    if a>lc:
        lc = a
        n = t
    t += 1
print(n,a)

print("time :", time.time()-start)