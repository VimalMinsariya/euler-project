import time
start=time.time()

def main1():
    def g(n,k):
        if k == 1 or k == n:
            return 1
        else:
            if n < k:
                return 0
            else:
                t = 0
                for i in range(k):
                    t += g(n-k,k-i)
                return t

    def f(n):
        t = 0
        for i in range(1,n):
            t += g(n,n-i)
        return t

    print(f(100))

def main2():
    charateristicf = {1: [1, -1]}
    a = [1,1]
    n = 2
    while n<101:
        f = charateristicf[n-1]
        x1 = f + [0] * n
        x2 = [0] * n + f
        result = []
        for j in range(len(x1)):
            result.append(x1[j] - x2[j])
        charateristicf[n] = result
        t = 0
        for j in range(1, n + 1):
            t -= charateristicf[n][j] * a[n - j]
        a.append(t)
        n += 1
    print(t-1)

main2()

print(time.time()-start)