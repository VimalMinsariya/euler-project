def isOdddigits(n):
    q, r = divmod(n, 10)
    if r%2 == 0: return False
    while q > 0:
        q, r = divmod(q, 10)
        if r%2 == 0: return False
    return True

def listToNumber(li):
    s = 0
    for n in li:
        s = 10*s+n
    return s

def reversibleTest(l_n, k):
    global length
    global cnt
    si = 0
    if k == 0: si = 1
    if k < length/2 and k != (length-1)/2:
        for i in range(si,10):
            l_n[k] = i
            for j in range(si,10):
                l_n[-1-k] = j
                n, rn = listToNumber(l_n[-1-k:]), listToNumber(l_n[k::-1])
                if isOdddigits(n+rn):
                    reversibleTest(l_n,k+1)
    elif k == (length-1)/2:
        for i in range(si,10):
            l_n[k] = i
            n, rn = listToNumber(l_n[-1-k:]), listToNumber(l_n[k::-1])
            if isOdddigits(n+rn):
                reversibleTest(l_n,k+1)
    else:
        t = listToNumber(l_n) + listToNumber(l_n[-1::-1])
        if isOdddigits(t):
            cnt += 1
    return cnt

total = 0
for length in range(5,6):
    cnt = 0
    l_n = [0]*length
    total += reversibleTest(l_n, 0)
    print(length)

print(total)
