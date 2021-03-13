def delta(u):
    l = len(u)
    re = []
    for i in range(1,l):
        re.append(u[i]-u[i-1])
    return re

def fit(u):
    l = len(u)
    if l == 1: return u[0]
    return u[-1]+fit(delta(u))

def seq(n):
    v = (1-(-n)**11)//(1+n)
    return v

v = []
s = 0
for i in range(1,11):
    v.append(seq(i))
    s += fit(v)

print(s)