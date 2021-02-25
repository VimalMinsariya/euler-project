import time
start = time.time()

# nthe_root(n) : length l below 1
def lys_root(m,n:int ,l:int) -> str:
    def difference(r, s, n):
        return (10 * r + s) ** n - (10 * r) ** n
    result = ''
    R,r,k = m,0,1
    while k < l + 1:
        p = 0
        test = 1
        while test > 0:
            test = R - difference(r,p,n)
            p += 1
        s = p - 2
        if k == 1:
            result += str(s) + '.'
        else:
            result += str(s)
        R = (R - difference(r,s,n))*(10**n)
        r = 10 * r + s
        k += 1
    return result

sum = 0
for i in range(100):
    k = i ** (1/2)
    if k != int(k):
        t = lys_root(i,2,100)
        j = 0
        for n in t:
            if n != '.' and j < 100:
                sum += int(n)
                j += 1
print(sum)

print(time.time()-start)