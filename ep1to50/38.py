import time
start = time.time()

pan_digits = [i for i in range(1,10)]

def digits(n):
    result = []
    while n > 0:
        result.append(n%10)
        n = n // 10
    return result

def Subtractable(v,w):
    result = True
    for i in w:
        if i in v:
            v.remove(i)
        else:
            result = False
            break
    return [result,v]

n = 1
while n < 12345:
    k = 1
    test = True
    b = [i for i in range(1,10)]
    while test:
        a = Subtractable(b,digits(n*k))
        if a == [True,[]]:
            print(n)
        test = a[0]
        b = a[1]
        k += 1
    n += 1

print(pan_digits)
print(time.time()-start)