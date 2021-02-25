import time
start = time.time()

s={0:1}
k = 1
for i in range(1,10):
    k *= i
    s[i] = k

def factorial_sum(n):
    result = 0
    while n > 0:
        result += s[n%10]
        n //= 10
    return result

def w(n):
    result = 1
    cycle = [n]
    while factorial_sum(n) not in cycle:
        n = factorial_sum(n)
        result += 1
        cycle.append(n)
    return result

def path(n):
    memo = {n:1}
    k = factorial_sum(n)
    test = True
    while test:
        if k in d:
            for i in memo:
                memo[i] += d[k]
            test = False
        else:
            if k not in memo:
                for i in memo:
                    memo[i] += 1
                memo[k] = 1
            else:
                equal = memo[k]
                for i in memo:
                    if memo[i] < equal:
                        memo[i] = equal
                test = False
        k = factorial_sum(k)
    return memo

d = {}
for i in range(1,10**6):
    if i not in d:
        k = path(i)
        for j in k:
            d[j] = k[j]

cnt = 0
max = 0
for i in d:
    if d[i] > max:
        max = d[i]
        n_max = i

d= {}
print(path(1479))

print(time.time()-start)