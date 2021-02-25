import time
start = time.time()

def setOfdivisor(n):
    result = []
    limit = int(n**(1/2))
    i = 1
    while i <= limit:
        if n % i == 0:
            result.append(i)
        i += 1
    return result

def n_sol(p):
    result = 0
    if p%2 == 0:
        for i in setOfdivisor((p**2)/2):
            test = i + (p**2)/(2*i)
            if test > p and test < 2*p:
                result += 1
    return result

max = 0
max_p = 1
for p in range(1001):
    if n_sol(p) > max:
        max = n_sol(p)
        max_p = p

print(max_p)

print('Elapsed Time:',time.time()-start)