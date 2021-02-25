import time
start = time.time()

def tolist(n):
    list = [0,0,0,0,0,0,0,0,0,0]
    test = n
    while test > 0:
        test, r = divmod(test,10)
        list[r] += 1
    return tuple(list)

index = {}
n = 1
success = False
while not success:
    k = tolist(n**3)
    if k in index:
        index[k].append(n)
        if len(index[k]) == 5:
            success = True
    else:
        index[k] = [n]
    n += 1

print(index[k][0]**3)

print(time.time()-start)