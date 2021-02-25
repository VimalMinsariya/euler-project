import math
import time

start = time.time()


def test357(n):
    result = True
    limit = math.sqrt(n + 1)
    d = 1
    while d < limit:
        q, r = divmod(n, d)
        if r == 0:
            v = d + q
            if not isPrime(v):
                result = False
                break
        d += 1
    return result


def isPrime(n):
    if n in memo:
        return True
    else:
        result = True
        limit = math.sqrt(n + 1)
        if n % 2 == 0:
            result = False
        else:
            k = 3
            while k < limit:
                if n % k == 0:
                    result = False
                    break
                k += 2
            if result:
                memo.add(n)
        return result


memo = {2, 3, 5, 7, 11}
print(test357(50))
sum = 3
N = 10 ** 8
for n in [6, 10, 22, 30, 34]:
    print(n)
    while n < N:
        if isPrime(n+1):
            if test357(n):
                sum += n
        n += 36
    print(time.time() - start)
    start = time.time()
print(sum)

print(time.time() - start)
