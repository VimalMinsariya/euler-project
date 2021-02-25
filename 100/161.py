type = [[[0,0],[0,1],[1,0]],\
        [[0,0],[0,1],[1,1]],\
        [[0,0],[1,0],[1,1]],\
        [[0,1],[1,0],[1,1]],\
        [[0,0],[1,0],[2,0]],\
        [[0,0],[0,1],[0,2]]]

M, N = 9, 12
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

R = len(row)
result = 0
pos = [i for i in range(R)]
next_pos_depth = {}
p = {}
for i in range(36):
    p[i] = 0
depth = {}
d = 0
while p[0] < R:
    depth[0] = [pos[p[0]]]
    next_pos_depth[0] = pos_row(depth[0])
    test = True
    while test:
        if len(next_pos_depth[d]) > 0:
            d += 1
            depth[d] = depth[d-1] + [next_pos_depth[d-1][p[d]]]
            next_pos_depth[d] = pos_row(depth[d])
        else:
            if d == 35:
                result += 1
                print('==',result,depth[d])
            if d == 0:
                npd = pos
            else:
                npd = next_pos_depth[d-1]
            if p[d] + 1 < len(npd):
                p[d] += 1
            else:
                if d>0:
                    p[d] = 0
                    d -= 1
                    p[d] += 1
            d -= 1
        if d == -1:
            d = 0
            test = False

print(result)