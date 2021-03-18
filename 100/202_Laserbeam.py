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

def mcnt(m,p,r):
    return (m-r)//p+1

def inverse3(p):
    if p == 2:
        return 1
    else:
        k, r = divmod(p,3)
        if r == 1:
            return (-k)%p
        else:
            return ((p//2)*k)%p

boff = 12017639147
k = (boff+3)//2
# 3으로 나누어 나머지가 -k%3인 수의 갯수
t = (-k)%3
n = mcnt(k,3,t)
m = n - 1
li = factorization(k)
sign = {1:-1}
sum = 0
for p in li:
    temp = dict()
    for s in sign:
        temp[s*p] = -sign[s]
        r = (inverse3(s*p)*(k%3))%(s*p)
        sum += temp[s*p]*mcnt(m,s*p,r)
    sign.update(temp)


print(n - sum)
