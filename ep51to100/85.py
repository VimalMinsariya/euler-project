C = 2*10**6

def cnt_rect(m,n):
    return (m+1)*m*(n+1)*n//4

def approximatin(n):
    m = int(((4*C)/(n*(n+1)))**(1/2))
    if cnt_rect(m,n) > C:
        m -= 1
    return m

# m*n 격자
n = 1
m = approximatin(n)
max = 1999000
while m >= n:
    k = cnt_rect(m,n)
    if max < k:
        max = k
        print(m,n, m*n)
    n += 1
    m = approximatin(n)

print(cnt_rect(77,36))