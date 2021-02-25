type = [[[0,0],[0,1],[1,0]],\
        [[0,0],[0,1],[1,1]],\
        [[0,0],[1,0],[1,1]],\
        [[0,1],[1,0],[1,1]],\
        [[0,0],[1,0],[2,0]],\
        [[0,0],[0,1],[0,2]]]

M, N = 9, 2
def gen_row(type,co):
    result = []
    col_list = []
    m, n = co
    inside = True
    for i in type:
        x, y = i
        if x+m > M-1 or y+n > N-1:
            inside = False
        col_list.append(N*(x+m)+(y+n))
    if inside == True:
        for j in range(M*N):
            if j in col_list:
                result.append(1)
            else:
                result.append(0)
    return result

row = []
for t in type:
    for m in range(M):
        for n in range(N):
            k = gen_row(t,[m,n])
            if k != []:
                row.append(k)

def pos_row(sel_row):
    result = []
    cell_list = []
    for r in sel_row:
        for i in range(M*N):
            if row[r][i] == 1:
                cell_list.append(i)
    s = sel_row[-1] + 1
    while s < len(row):
        test = True
        for i in cell_list:
            if row[s][i] == 1:
                test = False
                break
        if test:
            result.append(s)
        s += 1
    return result

start = [0 for i in range(M*N)]
pos_next[0] = []
node(0,0) = list[[],pos_next[0]]
