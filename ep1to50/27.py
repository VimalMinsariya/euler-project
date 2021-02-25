import time
start=time.time()

def isPrime(n):
    if n<0:
        n = -n
    result = True
    limit = (n+1)**(1/2)
    if n % 2 == 0:
        result = False
    else:
        factor = 3
        while factor < limit:
            if n % factor == 0:
                result = False
                break
            factor += 2
    return result

def max_consequtive(a,b):
    cnt = 0
    if b>0:
        limit = b
    else:
        limit = -b
    n = 0
    while n < limit:
        p = n**2 + a*n + b
        if isPrime(p):
           cnt += 1
        else:
            break
        n += 1
    return cnt

b = -999
max = 0
max_a = -1000
max_b = b
while b < 1000:
    if isPrime(b):
        for a in range(-1000,1000):
            temp = max_consequtive(a,b)
            if temp > max:
                max = temp
                max_a = a
                max_b = b
    b += 2

print(max_a*max_b,max)

print("elapsed time= ",time.time()-start)