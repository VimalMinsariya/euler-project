def solveProductExpression(sofar, remain, divisor):
    if remain == 1:
        result.append(sofar)
    else:
        if sofar == []:
            limit = int(remain**(1/2)) + 1
            for d in divisor:
                if d < limit:
                    re = remain // d
                    solveProductExpression([d], re, divisor)
        else:
            last = sofar[-1]
            start_idx = divisor.index(last)
            if last <= remain:
                for d in divisor[start_idx:]:
                    if remain % d == 0:
                        so = sofar + [d]
                        re = remain // d
                        solveProductExpression(so, re, divisor)
    return result

def productExpression(n):
    list = divisor(n)
    global result
    result =[]
    k = solveProductExpression([],n,list)
    return k

def divisor(n):
    list = []
    for d in range(2,n):
        if n%d == 0:
            list.append(d)
    return list

def main():
    kth_number = dict()

    n = 4
    M = 12000
    while 11944 not in kth_number:
        for p_list in productExpression(n):
            k = len(p_list) + (n-sum(p_list))
            if k not in kth_number:
                kth_number[k] = n
        n += 1

    l = set()
    for key in range(2,M+1):
        l.add(kth_number[key])
        print(key,kth_number[key])

    print(sum(l))

main()