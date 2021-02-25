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

def digit(n):
    set = {}
    while n > 0:
        r = n % 10
        if r not in set:
            set[r] = 1
        else:
            set[r] += 1
        n //= 10
    return set

digit4prime = []
for i in range(10**3,10**4):
    if isPrime(i):
        digit4prime.append(i)

pos = len(digit4prime)

for i in range(1,pos-1):
    prime2 = digit4prime[i]
    test = digit(prime2)
    for j in range(i):
        prime1 = digit4prime[j]
        if digit(prime1) == test:
            k = 2*prime2 - prime1
            if k in digit4prime and digit(k) == test:
                print(prime1*(10**8) + prime2*(10**4) + k)

print(time.time()-start)