def isCube(n):
    a = int(n**(1/3))
    if n == a**3 or n == (a+1)**3:
        return True
    return False

def recPermute(sofar, rest):
    if len(rest) == 0:
        per.append(sofar)
    else:
        for i in range(len(rest)):
            remain = rest[:i] + rest[i+1:]
            recPermute(sofar+rest[i], remain)
    return per

def permute(n):
    sofar = ''
    rest = str(n)
    global per
    per = []
    result = list(filter(lambda x: x[0] != '0', recPermute(sofar,rest)))
    result = list(map(lambda x: int(x), result))
    result = list(filter(lambda x: x >= n, result))
    return list(set(result))

def cube_count(n):
    cnt = 0
    list = permute(n**3)
    for k in list:
        if isCube(k):
            cnt += 1
    return cnt

n = 1
max = 1
while cube_count(n) != 5:
    if max < cube_count(n):
        max = cube_count(n)
    n += 1
    print(n, cube_count(n), max)

print(n, n**3)