def isBouncy(n):
    s = sorted(str(n))
    ni, nd = '', ''
    for nu in s:
        ni = nu + ni
        nd += nu
    ni, nd = int(ni), int(nd)
    if n in [ni,nd]:
        return False
    return True

proportion100 = 0
nBouncy = 0
n = 0
while proportion100 != 99:
    n += 1
    if isBouncy(n): nBouncy += 1
    proportion100 = nBouncy*100/n
print(n, proportion100)