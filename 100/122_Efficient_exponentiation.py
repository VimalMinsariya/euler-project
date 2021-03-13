def next_node(v):
    re = []
    for i in range(len(v)):
        re.append(v[i]+v[-1])
    return re

test = []
for i in range(2, 201):
    test.append(i)

ee = {1:0}

node= [[1]]
min = 1

while len(test) != 0:
    list = []
    for v in node:
        w = next_node(v)
        for a in w:
            if a in test:
                test.remove(a)
                ee[a] = min
                t = v + [a]
                list.append(t)
    node = list
    min += 1
    print(min, len(test))

res = sorted(ee.items())
s = 0
for j, k in res:
    print(f'm({j})={k}')
    s += k
print(s)



