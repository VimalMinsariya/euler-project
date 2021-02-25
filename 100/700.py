a = 1504170715041707
p = 4503599627370517
#a, p = 13, 57

def reciprocal(a,b): # a * x = 1 (mod b), find x < b
    h, i = a, b
    l = [1,0]
    m = [0,1]
    q, r = divmod(h,i)
    n = [l[0]-q*m[0], l[1]-q*m[1]]
    while r > 1:
        l, m = m, n
        h = l[0] * a + l[1] * b
        i = m[0] * a + m[1] * b
        q, r = divmod(h,i)
        n = [l[0]-q*m[0], l[1]-q*m[1]]
    assert (a*n[0])%b == 1
    return n[0]%b

eulercoins = [a]

def next_eulercoins(n):
    k = (p//n + 1)*n - p
    return k

while eulercoins[-1] != 1:
    k = eulercoins[-1]
    eulercoins.append(next_eulercoins(k))

reci = reciprocal(a,p)
test = 0
eulercoins2 = {}
order = []
for i in eulercoins:
    t = (reci * i) % p
    order.append(t)
    eulercoins2[t] = i
    print(f'{t:16}, {i}')

order.sort()
test = a + 1
sum = 0
for i in order:
    k = eulercoins2[i]
    if k < test:
        test = k
        sum += k
        print(f'{i:16}, {k}')

print(sum)

