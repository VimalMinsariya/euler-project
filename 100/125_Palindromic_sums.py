def isPal(n):
    original = n
    re = 0
    while n > 0:
        n, r = divmod(n, 10)
        re = re*10 + r
    if re == original: return True
    return False

li_sos = [0,1]
sos = 1
li_re = set()

for i in range(2,10000):
    sos += i**2
    li_sos.append(sos)
    for j in range(i-1):
        k = sos - li_sos[j]
        if k < 10**8 and isPal(k):
            li_re.add(k)

print(li_re, sum(li_re))