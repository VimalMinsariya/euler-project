import time
start=time.time()

pandigital9 = set()

def setted(i) -> set:
    a=set([int(t) for t in str(i)]) - {0}
    return a

def panproduct(m,n):
    for i in range(10**(m-1), 10**m):
        for j in range(10**(n-1), 10**n):
            a = setted(i)
            b = setted(j)
            if len(a) == m and len(b) == n:
                product = i * j
                c = setted(product)
                if product < 10**(9-m-n) and a | b | c == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    pandigital9.add(product)

panproduct(1,4)
panproduct(2,3)
print(sum([i for i in pandigital9]))

print("Elapsed Time: ",time.time()-start)