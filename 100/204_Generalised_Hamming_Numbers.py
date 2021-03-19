def esieve(n):
    li = [0,0] + [i for i in range(2,n+1)]
    sieve = []
    k = 0
    while k < n+1:
        if li[k] != 0:
            sieve.append(li[k])
            p = 2*k
            while p < n+1:
                li[p] = 0
                p += k
        k += 1
    return sieve

type = [1]
prime = esieve(100)
for p in prime:
    temp = []
    for j in type:
        v = j*p
        while v <= 10**9:
            temp.append(v)
            v *= p
    type = type + temp
print(len(type))
