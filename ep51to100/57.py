import time
start = time.time()

def digits(n):
    return len(str(n))

N=1000
a=[2]
b=[1]

for i in range(1,N):
    a_after = 2*a[-1]+b[-1]
    b_after = a[-1]
    a.append(a_after)
    b.append(b_after)

cnt = 0
for i in range(N):
    if digits(a[i]+b[i]) > digits(a[i]):
        cnt += 1
        print(cnt,a[i]+b[i],a[i])


print(cnt)

print('Elapsed Time:',time.time()-start)