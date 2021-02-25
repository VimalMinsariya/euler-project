import time
from decimal import *

start = time.time()

def p(L,n):
    a = Decimal(L).log10() / Decimal(2).log10()
    b = Decimal(L+1).log10() / Decimal(2).log10()
    cnt = 0
    i = 0
    k = Decimal(1) / Decimal(2).log10()
    while cnt != n:
        t = i * k
        left = t + a
        right = t + b
        if int(left) != int(right):
            cnt += 1
        i += 1
    return int(right)

getcontext().prec=28
for i in range(1,10):
    print(p(123,i))

print(time.time()-start)