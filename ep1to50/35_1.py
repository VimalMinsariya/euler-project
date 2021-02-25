import time
start=time.time()

def combinations(A, n):
    if n == 1: return [[el] for el in A]
    C = []
    for arr in combinations(A, n-1):
        for el in A: newarr = arr[:]; newarr.append(el); C.append(newarr)
    return C

def isprime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0: return False
    return True

P, cnt = [2, 3, 5, 7], 0
for i in range(2, 7):
    C = combinations([1, 3, 7, 9], i)
    for c in C: P.append(int(''.join([str(i) for i in c])))

for p in P:
    cir, s = True, str(p)
    for i in range(len(s)):
        if not isprime(int(s[i:]+s[:i])): cir = False; break
    if cir: cnt += 1
print(cnt)


print("Elapsed Time: ",time.time()-start)