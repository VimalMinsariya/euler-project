def isZahlen(a):
    if a==int(a):
        return True
    else:
        return False

def two_list(a):
    result=[]
    result.append(a[0]+a[1])
    result.append(a[0]-a[1])
    result.append(a[0]*a[1])
    if a[1] != 0 :
        result.append(a[0]/a[1])
    result.append(a[1]-a[0])
    if a[0] != 0:
        result.append(a[1]/a[0])
    return result

def three_list(a):
    result=[]
    temp1=two_list([a[0],a[1]])
    temp2 = two_list([a[1], a[2]])
    temp3 = two_list([a[2], a[0]])
    for i in temp1:
        result += two_list([i,a[2]])
    for i in temp2:
        result += two_list([i, a[0]])
    for i in temp3:
        result += two_list([i,a[1]])
    return result

def four_list(a):
    result=[]
    temp1 = two_list([a[0], a[1]])
    temp2 = two_list([a[0], a[2]])
    temp3 = two_list([a[0], a[3]])
    temp4 = two_list([a[1], a[2]])
    temp5 = two_list([a[1], a[3]])
    temp6 = two_list([a[2], a[3]])
    for i in temp1:
        result += three_list([i,a[2],a[3]])
    for i in temp2:
        result += three_list([i, a[1], a[3]])
    for i in temp3:
        result += three_list([i,a[1],a[2]])
    for i in temp4:
        result += three_list([i,a[0],a[3]])
    for i in temp5:
        result += three_list([i, a[0], a[2]])
    for i in temp6:
        result += three_list([i,a[0],a[1]])
    return result

def final_list(a):
    result=[]
    for i in a:
        if (i not in result) and (i>0) and (isZahlen(i)):
            result.append(int(i))
    return result

from itertools import combinations

max=0
r=range(1,11)
for a in combinations(r,4):
    result = sorted(final_list(four_list(list(a))))
    k=1
    while k in result:
        k=k+1
    if k>max:
        max=k
        print(list(a),max-1)

# print(sorted(final_list(four_list([1,2,5,8]))))