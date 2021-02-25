import time
start = time.time()

def compute(n):
    phi = [i for i in range(n + 2)]
    for p in range(2, n + 1):
        if phi[p] == p:
            phi[p] = p - 1
            for i in range(2 * p, n + 1, p):
                phi[i] = (phi[i] // p) * (p - 1)
    for i in range(2, n + 1):
        if sorted(list(str(i))) == sorted(list(str(phi[i]))):
            dic[i] = phi[i]


dic = dict()
n = 10000000
compute(n)
print(min(dic, key=lambda x: x / dic[x]))

print(time.time()-start)