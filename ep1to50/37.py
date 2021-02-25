def isPrime(n):
    result = True
    limit = int((n+1)**(1/2))
    if n < 2:
        result = False
    elif n == 2:
        result = True
    elif n > 2 and n%2 == 0:
        result = False
    else:
        k = 3
        while k <= limit:
            if n % k == 0:
                result = False
                #print(k)
                break
            k += 2
    return result

def isTP(n):
    result = True
    t = 1
    q = 10
    while q > 9:
        q = n // (10**t)
        r = n % (10**t)
        if (isPrime(q) == False) or (isPrime(r) == False):
            result = False
            break
        t += 1
    if isPrime(n) == False:
        result = False
    return result

sum = 0
cnt = 0
for i in range(13,1000000):
    if isTP(i) == True:
        sum += i
        cnt += 1
        print(cnt, i)
print(sum)