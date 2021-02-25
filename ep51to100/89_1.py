import time
from itertools import combinations_with_replacement as cwr
start = time.time()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def square_sum(n):
    result = 0
    son = str(n)
    for i in son:
        result += (int(i))**2
    return result

memo_89 = set()
r = 1
while r < 9**2 * 7 + 1:
    test = r
    while test not in [1,89]:
        test = square_sum(test)
    if test == 89:
        memo_89.add(r)
    r += 1

print(time.time() - start)

a = cwr('0123456789',7)
print(time.time() - start)
cnt = 0
N = factorial(7)
for i in a:
    square_sum = 0
    n = {}
    for j in i:
        if j not in n:
            n[j] = 1
        else:
            n[j] += 1
        square_sum += int(j)**2
    if square_sum in memo_89:
        t = 1
        for k in n:
            t *= factorial(n[k])
        cnt += N//t

print(cnt)

print(time.time()-start)