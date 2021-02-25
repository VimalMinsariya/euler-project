import time
start=time.time()

factorial=[1]
t=1
for i in range(1,10):
   t *= i
   factorial.append(t)

sum=0

for i in range(10,10**6):
    k = 0
    for j in str(i):
        k += factorial[int(j)]
    if i == k:
        print(i,end=',')
        sum += i
print("\n sum=",sum)

print("Elapsed Time: ",time.time()-start)