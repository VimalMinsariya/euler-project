from itertools import permutations as per

def outerset(arr):
    return [10]+arr[:4]

def innerset(arr):
    return arr[4:]

def fivegonset(arr):
    solset =[]
    outer = outerset(arr)
    inner = innerset(arr)
    for i in range(5):
        a, b, c = i, i, (i+1)%5
        line = [outer[a],inner[b],inner[c]]
        solset.append(line)
    return solset

def ismagic(solset):
    test = sum(solset[4])
    for i in range(4):
        if sum(solset[i]) != test: return False
    return True

def minsol(solset):
    re = ''
    min, min_value = 0, solset[0][0]
    for i in range(5):
        if solset[i][0] < min_value:
            min, min_value = i, solset[i][0]
    for i in range(5):
        a = (i+min)%5
        re += str(solset[a][0]) + str(solset[a][1]) + str(solset[a][2])
    return int(re)

start_arr = [1,2,3,4,5,6,7,8,9]

magicsol = []
for arr in per(start_arr,len(start_arr)):
    solset = fivegonset(list(arr))
    if ismagic(solset):
        magicsol.append(minsol(solset))
print(max(magicsol))