def C(n,r):
    if r in [0,n]: return 1
    else:
        if n-r < r: r = n-r
        nu, de = 1, 1
        for i in range(r):
            nu *= (n-i)
            de *= (i+1)
        return nu//de

def H(n,r):
    return C(n+r-1,r)

def ni(n):
    return H(10,n) - 1

def nd(n):
    v = 0
    for r in range(1,n+1):
        v += H(9,r)*(n-r+1)
    return v

def nNonBouncy(n):
    return ni(n)+nd(n)-9*n

print(nNonBouncy(100))

