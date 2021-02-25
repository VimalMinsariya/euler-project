import time
start=time.time()

from math import sqrt

def sum_pdivisor(n):
    if n<2:
        return
    sum=1
    b=int(sqrt(n))
    for i in range(2,b+1):
        if n%i == 0:
            sum += i
            if n%b != 0:
                sum += int(n/i)
    return sum

sum=0
for i in range(2,10000):
   a=sum_pdivisor(i)
   b=sum_pdivisor(a)
   if b == i and i < a and a<10000:
       print (i,'and',a,'are amicable numbers!')
       sum += i + a

print(sum)
print("Elapsed Time: ",time.time()-start)