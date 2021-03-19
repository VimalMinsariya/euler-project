def isSquarefree(n):
    p = 2
    limit = (n+1)**(1/2)
    while p < limit:
        cnt = 0
        while p < limit:
            if n % p == 0:
                n = n // p
                cnt += 1
            else:
                break
        if cnt > 1:
            return False
        p += 1
    return True

pt = dict()
N = 51
for row in range(N):
    for col in range(N-row):
        if row == 0 or col == 0:
            pt[(row,col)] = 1
        else:
            pt[(row,col)] = pt[(row,col-1)]+pt[(row-1,col)]

pascal_list = set()
for value in pt.values():
    pascal_list.add(value)

test = list(pascal_list)
test.sort()

total = 0

for v in test:
    if isSquarefree(v): total += v

print(total)
