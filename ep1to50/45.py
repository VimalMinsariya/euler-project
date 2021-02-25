import time
start = time.time()

def isP(n):
    k = (1+(1+24*n)**(1/2))/6
    if k == int(k):
        return True
    else:
        return False

def isH(n):
    k = (1+(1+8*n)**(1/2))/4
    if k == int(k):
        return True
    else:
        return False

def T(n):
    return int(n*(n+1)/2)

t = 286
k = T(t)
while isP(k) == False or isH(k) == False:
    t += 1
    k = T(t)

print(k)

print(time.time()-start)