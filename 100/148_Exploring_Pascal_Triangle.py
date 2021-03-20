def pascal(n,p):
    pl = []
    for row in range(n):
        tmp = []
        for col in range(n):
            if row == 0 or col == 0:
                tmp.append(1)
            else:
                v = tmp[-1] + pl[row-1][col]
                tmp.append(v%p)
        pl.append(tmp)
    return pl

li = pascal(10,7)
for row in li:
    for col in row:
        print(col,end=' ')
    print('\r')

n = 10**9

def convert(n):
    vert = []
    while n>0:
        n, r = divmod(n, 7)
        vert = [r] + vert
    return vert

def f(convert):
    k = len(convert) - 1
    if len(convert) == 1:
        a = convert[0]
        return a*(a+1)//2
    else:
        a = convert[0]
        convert = convert[1:]
        v = (a*(a+1)//2)*(28**k) + (a+1)*f(convert)
        return v

z = (n*(n+1))//2
print(f(convert(n)))
print(z)
