import time
start = time.time()

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

def list_to_number(list):
    result = list[0]
    for i in list[1:]:
        result = 10*result + i
    return result

def number_to_list(n):
    result = []
    while n>0:
        result = [n%10] + result
        n = n//10
    return result

def test(list):
    c1 = (list_to_number(list[1:4]) % 2 == 0)
    c2 = (list_to_number(list[2:5]) % 3 == 0)
    c3 = (list_to_number(list[3:6]) % 5 == 0)
    c4 = (list_to_number(list[4:7]) % 7 == 0)
    c5 = (list_to_number(list[5:8]) % 11 == 0)
    result = c1 and c2 and c3 and c4 and c5
    return result

plist=[]
for i in range(1,int(1000//17)+1):
    k = 17*i
    if k < 100:
        lk = [0]+number_to_list(k)
    else:
        lk = number_to_list(k)
    for j in range(1,int(1000//13)+1):
        l = 13 * j
        if l < 100:
            ll = [0] + number_to_list(l)
        else:
            ll = number_to_list(l)
        if lk[:2] == ll[1:]:
            if len(set(ll+[lk[2]])) == 4:
                plist.append(ll+[lk[2]])

result=[]

for pl in plist:
    p = []
    for i in range(10):
        if i not in pl:
            p.append(i)
    per = permutation(p,6)
    for permute in per:
        t = permute + pl
        if test(t) and t[0] != 0:
            result.append(t)

sum = 0
for i in result:
    sum += list_to_number(i)
print(sum)

print(time.time()-start)