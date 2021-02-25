import time
import copy
start = time.time()
seive_list = dict()
Limit = 2**50
limit = int(Limit**(1/2))
result = Limit
mju = {1:1}


for i in range(2,limit+1):
    seive_list[i] = True
for p in seive_list:
    if seive_list[p] == True:
        tmp = copy.deepcopy(mju)
        for k in tmp:
            if k*p < limit+1:
                mju[k*p] = -mju[k]
        if p <= int(limit**(1/2)):
            plus = 2*p
            while plus < limit+1:
                seive_list[plus] = False
                plus += p
    if p in mju:
        result += mju[p] * (Limit // (p ** 2))
        print(p)

print(result)
print(time.time()-start)