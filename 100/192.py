import time
start = time.time()

def next_range(n,r):
    r1, r2 = r
    a, b = r1
    c, d = r2
    p, q = a+c, b+d
    m = int(n**(1/2))
    d = (p+m*q)**2 - (q**2)*n
    if d > 0:
        return [r1, (p,q)]
    else:
        return [(p,q), r2]

def close_de(n,r):
    r1, r2 = r
    a, b = r1
    c, d = r2
    m = int(n**(1/2))
    d1 = ((b*d)**2)*n - (a*d+m*b*d)**2
    d2 = (b*c+m*b*d)**2 - ((b*d)**2)*n
    if d1 < d2:
        return b
    else:
        return d

def close_de_bound(n,MAX):
    r=[(0,1),(1,1)]
    de = 1
    while de <= MAX:
        result = close_de(n, r)
        r = next_range(n,r)
        de = max(r[0][1], r[1][1])
    return result

MAX = 10**12
limit = 10**5
result = 0
for i in range(2,limit+1):
    sqrt = i**(1/2)
    if sqrt != int(sqrt):
        result += close_de_bound(i,MAX)
print(result)
print(time.time()-start)

