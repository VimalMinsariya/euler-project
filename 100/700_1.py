def next_eulercoin(a,p):
    q, r = divmod(p, a)
    if r == 0:
        return 0
    else:
        e = a - r
        return e

a, p = 1504170715041707, 4503599627370517
eulercoins = [a]
while next_eulercoin(a,p) != 0:
    v = next_eulercoin(a,p)
    eulercoins.append(v)
    a, p = v, a

print(sum(eulercoins))