import time
start=time.time()

def isqf(a):
    t = (10*a[2]+a[0])*a[1] - (10*a[0]+a[1])*a[2]
    if t == 0:
        return True
    else:
        return False

n = [[a,b,c] for a in range(1,10) for b in range(1,10) for c in range(1,10)]

for i in n:
    if i[0] != i[1] and isqf(i) == True:
        print(10*i[2]+i[0],"/",10*i[0]+i[1],"=",i[2],"/",i[1])

print("Elapsed Time: ",time.time()-start)