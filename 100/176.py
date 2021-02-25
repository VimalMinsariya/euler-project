# 연필과 종이로 해결했음.

def factorization(n:int) -> dict:
    result = {}
    p = 2
    limit = (n+1)**(1/2)
    while p < limit:
        cnt = 0
        while p < limit:
            if n % p == 0:
                n = n // p
                cnt += 1
            else:
                break
        if cnt > 0:
            result[p] = cnt
        limit = (n+1)**(1/2)
        p += 1
    if n > 1:
        result[n] = 1
    return result

print(factorization(2*47547+1))
a = 2**10
b = 3**6
c = 5**5
d = 7**3
e = 11**2
print(a*b*c*d*e)

