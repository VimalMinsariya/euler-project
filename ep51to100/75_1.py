import time
start = time.time()

def gcd(m,n):
    if m < n:
        return gcd(n,m)
    else:
        if n == 0:
            return m
        else:
            return gcd(n,m%n)

def cnt_solution(n:int) -> list:
    N = int((n/2)**(1/2))+1
    result = [0]*(n+1)
    for i in range(2,N):
        for j in range(1,i):
            if gcd(i,j) == 1 and (i*j)%2 == 0:
                length = 2*i*(i+j)
                k = 1
                while length * k < n+1 :
                    result[length * k] += 1
                    k += 1
    return result

a = int(15e5)
cnt = 0
for i in cnt_solution(a):
    cnt += (i == 1)
print(cnt)

print(time.time()-start)
