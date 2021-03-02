def isOptimum(S):
    rank = len(S)
    for i in range(1,(rank+1)//2):
        if sum(S[:i+1]) <= sum(S[-i:]): return False
    li = []
    for i in range(1,2**rank):
        mask = []
        n = i
        for k in range(rank):
            n, r = divmod(n, 2)
            mask += [r]
        v = 0
        for k in range(rank):
            v += S[k]*mask[k]
        li.append(v)
    if len(set(li)) == 2**rank-1:
        print(S, sum(S))
        return True
    return False

with open('p105_sets.txt', 'r') as f:
    file = f.readlines()

v = 0
for se in file:
    S = sorted([int(a) for a in se.strip('\n').split(',')])
    if isOptimum(S):
        v += sum(S)
print(v)