def next_node(v):
    re = []
    for i in range(len(v)):
        re.append(v[i]+v[-1])
    return re

test, test2 = [], []
for i in range(2, 201):
    test.append(i)
    test2.append(i)

ee = {1:0}
ee2 = {1:0}

node, node2 = [[1]], [[1]]
min, min2 = 1, 1

while len(test) != 0:
    list, list2 = [], []
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
    for v in node2:
        w = next_node(v)
        for a in w:
            if a in test:
                test2.remove(a)
                ee2[a] = min2
                t = v + [a]
                list2.append(t)
    node2 = list2
    min2 += 1

res = sorted(ee.items())
s = 0
for j, k in res:
    print(f'm({j})={k}',ee2[j])
    s += k
print(s)



