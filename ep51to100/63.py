import time
start = time.time()

cnt = 0
for i in range(2,10):
    k = 10 / i
    n = 1
    while k ** n < 10:
        N = i**n
        nod = len(str(N)) # nod: number of digits
        if nod == n:
            print(i,'**',n,'=',N)
            cnt += 1
        n += 1

print(cnt)
print(time.time()-start)