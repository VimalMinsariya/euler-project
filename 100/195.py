import time
start = time.time()

def pri_ic_radius(m,n):
    r = 3 ** (1 / 2) * (m - n) * n / 2
    if (m+n)%3 == 0:
        r = r / 3
    return r

def gcd(m,n):
    if m < n:
        return gcd(n,m)
    else:
        if n == 0:
            return m
        else:
            return gcd(n,m%n)

def T(N):
    cnt = 0
    n = 1
    n_limit = 2*N/(3**(1/2))
    while n < 3 * n_limit:
        m = n + 1
        m_limit = (2*N)/((3**(1/2))*n)
        while m < n + 3 * m_limit:
            k = gcd(m,n)
            if k == 1:
                r = pri_ic_radius(m,n)
                k = int(N/r)
                if m==2 and n==1:
                    k = 0
                cnt += k
            m += 1
        n += 1
    return int(cnt/2)

N = 1053779
print(T(N))

print(time.time()-start)