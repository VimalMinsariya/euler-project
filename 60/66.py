def isSquare(n):
    m = n**(1/2)
    return m == int(m)

def min_sol(D):
    if isSquare(D):
        return 1
    else:
        y=1
        k = 1 + D*y**2
        while not isSquare(k):
            y += 1
            k = 1 + D * y ** 2
    return int(k**(1/2))

def square_divisor(n):
    result = set()
    i = 2
    while i**2 < n+1:
        p,q = divmod(n,i**2)
        if q == 0:
            result.add(p)
        i += 1
    return result

print(min_sol(61))
"""max = 0
blacklist = set()
for D in range(1000,1, -1):
    if D not in blacklist:
        blacklist = blacklist | square_divisor(D)
        k = min_sol(D)
        if k > max:
            max = k
            result = D
        print(D,k)
    else:
        print(D, 'blacklist')

print(result)"""