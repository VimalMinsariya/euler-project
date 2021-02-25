import time

start = time.time()

def isSquare(n):
    m = int(n**(1/2))
    if m**2 == n:
        return True
    else:
        return False

def isIntegerSide(p,q):
    c = p**2 + q**2 + p*q
    if isSquare(c):
        return True
    else:
        return False

count = 0
N = 120000
m=2
n=1
list=[]
list2=set()
while m**2 - n**2 < N:
    while 2*m*n + n**2 < N:
        k = 1
        while k*((2*m*n + n**2) + (m**2 - n**2)) < N:
            list.append({k*(m**2-n**2),k*(2*m*n+n**2)})
            list2 |= {k*(m**2-n**2),k*(2*m*n+n**2)}
            k += 1
            count += 1
        m += 1
    n += 1
    m = n + 1

solset = set()
for i in list2:
    same = []
    for j in list:
        if i in j:
            same.append(j)
    subcount = len(same)
    for m in range(subcount-1):
        for n in range(m+1,subcount):
            inter = same[m] ^ same[n]
            if len(inter) == 2:
                p = [k for k in inter]
                if isIntegerSide(p[0], p[1]):
                    union = same[m] | same[n]
                    sumofside = sum([l for l in union])
                    if sumofside <= N:
                        solset = solset | {sumofside}
                        print(union, sumofside)

print(sum([i for i in solset]))

"""sol = 0
solset = set()
solset_e = set()
for i in range(count-1):
    print('===',i,'===')
    for j in range(i+1,count):
        inter = list[i] & list[j]
        if len(inter) == 1:
            p = [k for k in (list[i] ^ list[j])]
            if isIntegerSide(p[0],p[1]):
                union = list[i] | list[j]
                sumofside = sum([l for l in union])
                if sumofside <= N:
                    solset_e |= solset & {sumofside}
                    solset = solset | {sumofside}
                    print(union, sumofside)
                    sol += sumofside

print(sum(i for i in solset))
print(sol)
print(solset_e)"""

"""def isTT(p,q,r):
    a2 = q**2 + r**2 + q*r
    if isSquare(a2):
        b2 = r**2 + p**2 + r*p
        if isSquare(b2):
            c2 = p**2 + q**2 + p*q
            if isSquare(c2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False"""

"""p=q=r=1
sum = 0
N= 120000
while p+q+r <= N:
    while p + q + r <= N:
        if isIntegerSide(p,q):
            while p + q + r <= N:
                if isIntegerSide(q,r) and isIntegerSide(r,p):
                    sum += p+q+r
                    print(p,q,r)
                r += 1
        q += 1
        r = q
    p += 1
    q = p
    r = p"""

print(time.time()-start)