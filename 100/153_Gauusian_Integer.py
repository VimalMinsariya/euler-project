def gcd(m,n):
    if m < n:
        return gcd(n,m)
    else:
        if n == 0:
            return m
        else:
            return gcd(n,m%n)

def mm(a,b):
    d = gcd(a,b)
    a1, b1 = a//d, b//d
    return d*(a1**2+b1**2)

def pairsum(a,b):
    if a == b:
        return (2*a)
    else:
        return (2*a+2*b)

def ss(a,b):
    k = pairsum(a,b)
    j = mm(a,b)
    sum = 0
    t = 1
    while j*t<=N:
        sum += (t*k)*(N//(t*j))
        t += 1
    return sum

sum = 0
N = 10**8
limit = int(N**(1/2))
for i in range(1,N+1):
    sum += i*(N//i)

for x in range(1,limit+1):
    print(x)
    for y in range(1,x+1):
        if gcd(x,y) == 1 and mm(x,y) <= N:
            sum += ss(x,y)

print(sum)
