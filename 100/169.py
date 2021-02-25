import time
start = time.time()

list = {0:0, 1:1, 2:2}
def f(n):
    if n in list:
        return list[n]
    else:
        if n % 2 == 0:
            m, k = n, 0
            while m % 2 == 0:
                m = m // 2
                k += 1
            list[n] = f(m) + k*f(m-1)
        else:
            m = n
            list[n] = f((m-1)//2)
    return list[n]

print(f(10))
print(time.time()-start)