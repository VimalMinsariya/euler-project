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

def combination(list,r):
    result = []
    if len(list) == r and r > 0:
        return [list]
    elif r == 0:
        return [[]]
    else:
        first = list[0]
        remLst = list[1:]
        for p in combination(remLst,r-1):
                result.append([first]+p)
        for p in combination(remLst,r):
                result.append(p)
        return result

matrix_txt='  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583 \
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913 \
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743 \
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350 \
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350 \
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803 \
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326 \
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973 \
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848 \
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198 \
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390 \
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574 \
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699 \
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107 \
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805 '

matrix=[]
row = 15
row_matrix = []
num=''
for i in matrix_txt:
    if i != ' ':
        num += i
    else:
        if num != '':
            row_matrix.append(int(num))
            if len(row_matrix) == row:
                matrix.append(row_matrix)
                row_matrix = []
            num = ''

def sub_matrix(matrix,list,n):
    result_matrix=[]
    col = len(list)
    for i in list:
        result_matrix.append(matrix[i-1][(n-1)*col:n*col])
    return result_matrix

def matrix_sum(matrix):
    max_sum = 0
    row = len(matrix)
    list = permutation([i for i in range(row)],row)
    for permute in list:
        sum = 0
        k = 0
        for i in permute:
            sum += matrix[i][k]
            k += 1
        if sum > max_sum:
            max_sum = sum
            #max_permute = permute
    return max_sum

def list_subtract(v,w):
    k = []
    for i in v:
        if i not in w:
            k.append(i)
    return k

a = [i+1 for i in range(15)]
list1 = combination(a,5)
max_sum = 0
cnt = 0

for list_first in list1:
    sub_matrix_first = sub_matrix(matrix,list_first,1)
    sum_first = matrix_sum(sub_matrix_first)
    b = list_subtract(a,list_first)
    list2 = combination(b,5)
    for list_second in list2:
        sum = 0
        sub_matrix_second = sub_matrix(matrix,list_second,2)
        sum_second = matrix_sum(sub_matrix_second)
        list_third = list_subtract(b,list_second)
        sub_matrix_third = sub_matrix(matrix, list_third,3)
        sum_third = matrix_sum(sub_matrix_third)
        sum = sum_first + sum_second + sum_third
        if sum > max_sum:
            max_sum = sum
            print(cnt, list_first,list_second, list_third, sum)
    cnt += 1

print(max_sum)

print(time.time()-start)
