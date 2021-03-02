import itertools

R = list(range(18,47))
sample = [21, 32, 39, 40, 41, 43, 46]

def isOptimum(S):
    rank = len(S)
    for i in range(1,(rank-1)//2):
        if sum(S[:i+1]) <= sum(S[-i:]): return False
    sumList = []
    for i in range(1,2**rank):
        mask = []
        n = i
        for k in range(rank):
            n, r = divmod(n, 2)
            mask += [r]
        sublist = []
        for k in range(rank):
            v = S[k]*mask[k]
            if v != 0: sublist.append(v)
        sumList.append(sum(sublist))
    if len(set(sumList)) == 2**rank-1: return True
    return False

sets = itertools.combinations(R,7)
min = sum(sample)
result = sample
for T in sets:
    S = list(T)
    if isOptimum(S):
        print('special subset:', S)
        if sum(S) < min:
            min = sum(S)
            result = S
print(result, min)