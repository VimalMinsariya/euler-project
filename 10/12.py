def d(n):
    k=0
    sqrt_n = n ** (1/2)
    for i in range(1,int(sqrt_n)+1):
        if n%i == 0:
            k += 2
    if n == int(sqrt_n) * int(sqrt_n):
        k -= 1
    return k

import time
start = time.time()

a=1
t=1
while d(t) <= 500:
    a += 1
    t += a

print(t)
print("time :", time.time()-start)