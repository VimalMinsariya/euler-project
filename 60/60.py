primes = [2,3,5,7,9]
test = []
pset = dict()

def limit(n):
    return int(n**(1/2)) + 1

n = 11
while p in list(filter(lambda prime: prime < limit(n), primes)):
    if n % p == 0:
        isPrime = False
        break
if isPrime == True:
    if len(str(n)) > len(str(primes[-1])):
        for p in test:
            k = str(p)
            for cut in range(1,len(k)):
                a, b = k[:cut], k[cut:]
                a, b, c = int(a), int(b), int(b+a)
                if a in primes and b in primes and c in primes:
                    if pset
        test = []
    primes.append(n)
    test.append(p)

n += 2
