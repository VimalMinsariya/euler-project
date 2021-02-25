import time
start = time.time()

def isPrime(n):
    result = True
    limit = (n+1)**(1/2)
    if n % 2 == 0:
        result = False
    else:
        k = 3
        while k < limit:
            if n % k == 0:
                result = False
                break
            k += 2
    return result

def prime_sieve(n):
    result=[]
    a = [i for i in range(n)]
    a[1] = 0
    for i in range(n):
        if a[i] != 0:
            result.append(a[i])
            t = 2*i
            while t < n:
                a[t] = 0
                t += i
    return result

def csum(k):
    result = [0]
    sum = 0
    for i in k:
        sum += i
        result.append(sum)
    return result

N = 10**6
max = 0
k = prime_sieve(N)
c = csum(k)

s = 0
while s<len(k)-1:
    i=1
    while c[s+i] - c[s] < N:
        if isPrime(c[s+i] - c[s]):
            if i > max:
                max = i
                max_prime = c[s+i] - c[s]
        i += 1
    s += 1

print(max,max_prime)

print(time.time()-start)