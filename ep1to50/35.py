import time
start=time.time()
N = 10**6
pr=[2,3]
pos=[0]
for i in range(5,N,2):
    isPrime = True
    j=0
    while pr[j] <= i ** (1/2):
        if i%pr[j] == 0:
            isPrime = False
            break
        j += 1
    if isPrime == True:
        if len(str(pr[-1]))<len(str(i)):
            pos.append(len(pr))
        pr.append(i)
pos.append(len(pr))
print(pr)
print(pos)
total = 0

for j in pr:
    s = str(j)
    l = len(s)
    t=0
    isCircular = True
    if '2' not in s:
        while t<l:
            s=s[-1:]+s[:-1]
            circular = int(s)
            if circular not in pr[pos[l-1]:pos[l]]:
                isCircular = False
                break
            t += 1
        if isCircular == True:
            total += 1
        #print(j)

print("\n",total+1)
print("Elapsed Time: ",time.time()-start)