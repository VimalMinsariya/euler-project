def splitting(n):
    ok = False
    k = n**2
    a = str(k)
    l = len(a) - 1
    for i in range(1,2**l):
        t = bin(i)
        b = str(t)[2:]
        add0 = l - len(b)
        b = '0'*add0 + b
        r = a[0]
        result = 0
        for j in range(l):
            if b[j] == '0':
                r += a[j+1]
            else:
                result += int(r)
                r = a[j+1]
        result += int(r)
        if result == n:
            ok = True
            break
    return ok

sum = 0
for N in range(1,10**6+1):
    if N%9 in [0,1] and splitting(N):
        print(N**2, N)
        sum += N**2

print(sum)





