def printMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    for row in range(m):
        for col in range(n):
            a = matrix[row][col]
            if a < INFINITY:
                print(f'{a:4d}',end=' ')
            else:
                print('inf',end='  ')
        print('\r')

def printDot(matrix):
    m, n = 5, 5
    dot = []
    for row in range(m):
        temp = []
        for col in range(n):
            temp.append('X')
        dot.append(temp)
    for i,j in matrix:
        dot[i][j] = 'O'
    for row in range(m):
        for col in range(n):
            print(dot[row][col],end=' ')
        print('\r')

def printRoute(matrix, paths):
    def lattice(m,n):
        if m%3 == 0 and n%3 == 0:
            return 'O'
        else:
            return ' '
    m, n = len(matrix), len(matrix[0])
    layout = [[lattice(row,col) for col in range(3*n-2)] for row in range(3*m-2)]
    for lattice, previous in paths.items():
        x, y = lattice
        u, v = previous
        if u < x : layout[3*x-2][3*y], layout[3*x-1][3*y] = '|', 'v'
        if u > x : layout[3*x+1][3*y], layout[3*x+2][3*y] = '^', '|'
        if v < y : layout[3*x][3*y-2], layout[3*x][3*y-1] = '-', '>'
        if v > y : layout[3*x][3*y+1], layout[3*x][3*y+2] = '<', '-'
    for row in range(3*m-2):
        for col in range(3*n-2):
            a = layout[row][col]
            print(a,end='')
        print('\r')

import urllib.request

webUrl  = urllib.request.urlopen('https://projecteuler.net/project/resources/p083_matrix.txt')
webmatrix = webUrl.readlines()
matrix = [list(map(int,row.decode('utf-8').split(',')[:20])) for row in webmatrix]
matrix = matrix[:20]

INFINITY = 1000000000

# matrix = [[131, 673, 234, 103, 18], \
#         [201, 96, 342, 965, 150], \
#         [630, 803, 746, 422, 111], \
#         [537, 699, 497, 121, 956], \
#         [805, 732, 524, 37, 331]]

size = len(matrix)
start = (0,0)
si, sj = start
visited = [[False for i in range(size)] for j in range(size)]
distances = [[INFINITY for i in range(size)] for j in range(size)]
distances[si][sj] = matrix[si][sj]
paths = dict()
queue = [(si, sj)]

while len(queue) > 0:
    i, j = min(queue, key=lambda v: distances[v[0]][v[1]])
    queue.remove((i, j))
    visited[i][j] = True
    neighbor = []
    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= ni < size and 0<= nj < size:
            neighbor.append((ni,nj))
    p, q = min(neighbor, key=lambda v: distances[v[0]][v[1]])

    if i != si or j != sj: paths[(i,j)] = (p,q)

    for ni, nj in neighbor:
        if not visited[ni][nj]:
            distances[ni][nj] = min(distances[ni][nj], distances[i][j] + matrix[ni][nj])

            if (ni, nj) not in queue:
                queue.append((ni, nj))

printMatrix(matrix)
print('\n')
printRoute(matrix,paths)
print('\n')
print(distances[-1][-1])
