import time
start=time.time()

N=100000

"""
k=N**(1/2)
pr=[i for i in range(2,N)]
i=0
while pr[i] <= k:
    j = 2
    while j*pr[i]<pr[-1]+1:
        if j*pr[i] in pr:
            pr.remove(j*pr[i])
        j += 1
    i += 1
pr.remove(2)
"""

pr=[2,3]
for i in range(5,N,2):
    isPrime = True
    j=0
    while pr[j] <= i ** (1/2):
        if i%pr[j] == 0:
            isPrime = False
            break
        j += 1
    if isPrime == True:
        pr.append(i)
pr.remove(2)

def remainder(p,m):
    r=1
    t=0
    while t<p :
        r *= 2
        if r >= m:
            r = r - m
        t += 1
    return r

def g(p):
    a = (remainder(p,p-1)-1)%(p-1)
    b = remainder(a,p)
    c = remainder(p,p**2)
    return ((c*b)//p)%p

sum = 0
for p in pr:
    sum += g(p)

print(sum)
#print(pr[:1000])

print("Elapsed Time: ",int(time.time()-start))