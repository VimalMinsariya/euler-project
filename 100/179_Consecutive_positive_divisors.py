dn = dict()
N = 10**7
for i in range(2,N):
    dn[i] = 1
for d in range(2,N):
    for n in range(d,N,d):
        dn[n] += 1
print('done')
cnt = 0
for n in range(2,N-1):
    if dn[n] == dn[n+1]: cnt += 1

print(cnt)
