from time import thread_time

def main():
    charateristicf = [1, -1]
    a = [1,1]
    n = 2
    while n < 50:
        f = charateristicf
        x1 = f + [0] * n
        x2 = [0] * n + f
        result = []
        for j in range(len(x1)):
            result.append(x1[j] - x2[j])
        charateristicf = result
        print(charateristicf)
        t = 0
        for j in range(1, n + 1):
            t -= charateristicf[j] * a[n - j]
        t = t%(10**6)
        a.append(t)
        print(n,t)
        n += 1
    print(n-1)

def main2():
    m = {1:1, 2:1}
    t = 1
    max_m = 2
    p = [1,1,2]
    n = 3
    while p[n-1] != 0:
        if n > max_m:
            t += 1
            v = (3*t**2 - t)//2
            if t%2 == 0:
                m[v], m[v+t] = -1, -1
            else:
                m[v], m[v + t] = 1, 1
            max_m = v+t
        k = 0
        for i in m:
            if i<=n:
                k += p[n-i]*m[i]
            else:
                break
        p.append(k%(10**6))
        print(n,p[n])
        n += 1
    print(n-1)
    print(thread_time())

main2()