def add(u,v):
    lu, lv = len(u), len(v)
    if lu + 1 == lv: u.insert(0,0)
    re = []
    push = 0
    for i in range(lv):
        a, b = u[-1-i], v[-1-i]
        push, r = divmod(a+b+push,10)
        re = [r] + re
    if push != 0: re = [push] + re
    return re

def isPal(n,p):
    pal = {1,2,3,4,5,6,7,8,9}
    if p == 'first':
        if set(n[:9]) == pal: return True
        return False
    if p == 'last':
        if set(n[-9:]) == pal: return True
        return False

f_first, f_second = [1], [1]
g_first, g_second = [1], [1]
m, n = [2], [2]
k = 2
while not isPal(m,'first') or not isPal(n,'last'):
    f_second, f_first = add(f_first,f_second), f_second
    if len(f_second) > 20: f_first, f_second = f_first[:19], f_second[:20]
    m = f_second
    g_second, g_first = add(g_first, g_second), g_second
    if len(g_second) > 9: g_second = g_second[-9:]
    n = g_second
    k += 1
    if k%1000 == 0: print(k)

print(k)

