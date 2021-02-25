tri = list(filter(lambda n : n>999 and n<10000, list(map(lambda n: n*(n+1)//2, range(141)))))
squ = list(filter(lambda n : n>999 and n<10000, list(map(lambda n: n**2, range(141)))))
pen = list(filter(lambda n : n>999 and n<10000, list(map(lambda n: n*(3*n-1)//2, range(141)))))
hex = list(filter(lambda n : n>999 and n<10000, list(map(lambda n: n*(2*n-1), range(141)))))
hep = list(filter(lambda n : n>999 and n<10000, list(map(lambda n: n*(5*n-3)//2, range(141)))))
opt = list(filter(lambda n : n>999 and n<10000, list(map(lambda n: n*(3*n-2), range(141)))))

list = [tri, squ, pen, hex, hep, opt]

a = [1,2,3,4,5]
def permutation(list,r):
    result = []
    if r == 0:
        return [[]]
    else:
        for i in range(len(list)):
            remLst = list[:i]+list[i+1:]
            for p in permutation(remLst,r-1):
                result.append([list[i]]+p)
        return result

order = permutation(a,5)

cycle_list = [0,0,0,0,0,0]
for p in order:
    for c0 in tri:
        cycle_list[0] = c0
        for c1 in list[p[0]]:
            if str(c0)[-2:] == str(c1)[:2]:
                cycle_list[1] = c1
                for c2 in list[p[1]]:
                    if str(c1)[-2:] == str(c2)[:2]:
                        cycle_list[2] = c2
                        for c3 in list[p[2]]:
                            if str(c2)[-2:] == str(c3)[:2]:
                                cycle_list[3] = c3
                                for c4 in list[p[3]]:
                                    if str(c3)[-2:] == str(c4)[:2]:
                                        cycle_list[4] = c4
                                        for c5 in list[p[4]]:
                                            if str(c4)[-2:] == str(c5)[:2] and str(c5)[-2:] == str(c0)[:2]:
                                                cycle_list[5] = c5
                                                print(cycle_list, p)
                                                print(sum(cycle_list))

