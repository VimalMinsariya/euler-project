def erthosthenes_sieve(n):
    prime = []
    sieve = {}
    for i in range(2,n+1):
        sieve[i] = 1
    p = 2
    while p < n+1:
        if sieve[p] == 1:
            prime.append(p)
            out= 2*p
            while out < n+1:
                sieve[out] = 0
                out += p
        p += 1
    return prime

limit = 5*10**7 + 1
prime = erthosthenes_sieve(7500)

good_number = set()

p2,p3,p4 = [],[],[]
for p in prime:
    if p**2 < limit:
        p2.append(p**2)
    if p**3 < limit:
        p3.append(p**3)
    if p**4 < limit:
        p4.append(p**4)

for q4 in p4:
    print(q4)
    for q3 in p3:
        for q2 in p2:
            k = q2 + q3 + q4
            if k < limit:
                good_number.add(k)
            else:
                break

print(len(good_number))
