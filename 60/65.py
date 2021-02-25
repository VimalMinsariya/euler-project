import time
start = time.time()

nth = 100
e = [2]
p = 1
while p < nth:
    if p % 3 == 2:
        e.append((p//3 + 1)*2)
    else:
        e.append(1)
    p += 1

def cf(a,b):
    return [a*b[0]+b[1],b[0]]

s = [e[-1],1]
for i in range(nth-1):
    s = cf(e[-i-2],s)

print(sum([int(i) for i in str(s[0])]))

print(time.time()-start)