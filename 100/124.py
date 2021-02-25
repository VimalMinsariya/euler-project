import time
start = time.time()

N=100000
setOfradical = [[i,1] for i in range(1,N+1)]
for i in range(N):
    if setOfradical[i][1] == 1:
        k = setOfradical[i][0]
        step = k
        while step < N+1:
            setOfradical[step-1][1] *= k
            step += k

unorderedSetOfradical = set()
for i in setOfradical:
    unorderedSetOfradical |= {i[1]}

sortedSetOfradical = []
k = []
for i in unorderedSetOfradical:
    k.append(i)
sortedSetOfradical = sorted(k)

target = 10000
cnt = 0
break_ok = False
for i in sortedSetOfradical:
    for j in setOfradical:
        if i == j[1]:
            cnt += 1
            if cnt == target:
                print(f'E({cnt}) = {j[0]}')
                break_ok = True
                break
    if break_ok == True:
        break

print('Elapsed Time:',time.time()-start)