import math
import itertools

A = 6 + math.log10(8)

P = [2,3,5,7,11,13,17,19,23,29,31,37,41]
E_temp = [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]

def logn(N):
    P, E = N
    rank = len(P)
    rn, rd = 0, 0
    for n in range(rank):
        rn += E[n]*math.log10(P[n])
        rd += math.log10(2*E[n]+1)
    return (rn,rd)

li = itertools.combinations_with_replacement((0,1,2,3,4),13)
min = logn((P,E_temp))[0]

for t in li:
    E = sorted(list(t), reverse=True)
    rn, rd = logn((P,E))
    if rd >= A:
        if rn < min:
            print(rn, rd)
            min = rn
            g = E

print(min,g)

sol = 1
for i in range(13):
    sol *= P[i]**g[i]

print(sol)