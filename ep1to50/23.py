def sumOfdivisor(n):
    sqrt_n = n**(1/2)
    sum = 0
    i=1
    while i <= sqrt_n:
        if i == sqrt_n:
            sum += int(sqrt_n)
            break
        if n%i == 0:
            sum += i + n/i
        i += 1
    return sum

def isAbundant(n):
    if sumOfdivisor(n) > 2*n:
        return True
    else:
        return False

import time
start = time.time()

alist={12}
twoSum={24}
N=28214
for i in range(1,N):
    if isAbundant(i):
        alist.add(i)
for i in alist:
    for j in alist:
        if i+j<28214:
            twoSum.add(i+j)

K=set(range(1,N))-twoSum
print(sum(K))
print(time.time()-start)
