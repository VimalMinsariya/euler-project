import time
start = time.time()

m = 10**9 + 7

r_list = [10]
for i in range(1,10):
    r_list.append((r_list[i-1]**10) % m)

def remain(q):
    t = 0
    result = 1
    while q > 0:
        q, r = divmod(q, 10)
        result *= (r_list[t]**r)%m
        result = result%m
        t += 1
    return result

def S(k):
    q, r = divmod(k,9)
    q = q % (m-1)
    result = (5+(r+1)*(r+2)//2)*remain(q) - (k+6)
    return result % m


f = {0:0, 1:1}
for i in range(2,91):
    f[i] = f[i-1] + f[i-2]

sum = 0

for i in range(2,91):
    k = S(f[i])
    print(i,f[i],k)
    sum += k

print(sum%m)
print(time.time()-start)