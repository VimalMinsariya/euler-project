import time
start = time.time()

def isPrime(n):
    result = True
    limit = (n+1)**(1/2)
    k = 0
    test = prime[k]
    while test < limit:
        if n % test == 0:
            result = False
            break
        k += 1
        test = prime[k]
    return result

prime = [2]
charateristicf = {2:[1,0,-1]}
a = [1,0,1]
ways = 5000
n = 3
t = 0
while t <= ways:
    if isPrime(n):
        pre_p = prime[-1]
        prime.append(n)
        f = charateristicf[pre_p]
        l = len(f)
        x1 = f + [0] * n
        x2 = [0] * n + f
        result = []
        for j in range(l+n):
            result.append(x1[j] - x2[j])
        charateristicf[n] = result
        t = 0
        for j in range(1,n+1):
            t -= charateristicf[n][j]*a[n-j]
        if t > ways:
            sol = n
        a.append(t)
    else:
        t = 0
        p = prime[-1]
        for j in range(1,n+1):
            t -= charateristicf[p][j]*a[n-j]
        if t > ways:
            sol = n
        a.append(t)
    n += 1

print(sol)

print(time.time()-start)