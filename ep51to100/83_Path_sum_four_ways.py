import urllib.request
import copy

def printMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    for row in range(m):
        for col in range(n):
            a = matrix[row][col]
            if a != 'inf':
                print(f'{a:4d}',end=' ')
            else:
                print(f'{a}',end='  ')
        print('\r')

webUrl  = urllib.request.urlopen('https://projecteuler.net/project/resources/p083_matrix.txt')
webmatrix = webUrl.readlines()
matrix = [list(map(lambda x: int(x),row.decode('utf-8').split(','))) for row in webmatrix]
# matrix = [[131, 673, 234, 103, 18], \
#         [201, 96, 342, 965, 150], \
#         [630, 803, 746, 422, 111], \
#         [537, 699, 497, 121, 956], \
#         [805, 732, 524, 37, 331]]

printMatrix(matrix)
print(dir(webmatrix[0]))

N, M = len(matrix[0]), len(matrix)
minimalSumMatrix = []
for row in range(M):
    temp =[]
    for col in range(N):
        temp.append('inf')
    minimalSumMatrix.append(temp)

class node:
    global matrix
    global minimalSumMatrix
    def __init__(self,P):
        self.index = P
    def neighborNode(self):
        m,n = self.index
        nodes = []
        if m > 0: nodes.append((m-1,n))
        if m < M-1: nodes.append((m+1,n))
        if n > 0: nodes.append((m,n-1))
        if n < N-1: nodes.append((m,n+1))
        return nodes
    def neighborValue(self):
        nv = []
        for nd in self.neighborNode():
            m, n = nd
            a = minimalSumMatrix[m][n]
            if a != 'inf':
                nv.append(a)
        return nv
    def previousNode(self):
        v = 'inf'
        result = 'None'
        for nd in self.neighborNode():
            row, col = nd
            t = minimalSumMatrix[row][col]
            if t != 'inf':
                if v == 'inf':
                    v = t
                    result = nd
                else:
                    if t < v:
                        v = t
                        result = nd
        return result
    def value(self):
        m,n = self.index
        a = self.previousNode()
        if a == 'None':
            v = matrix[0][0]
            minimalSumMatrix[0][0] = v
        else:
            row, col = a
            v = matrix[m][n]
            pv = minimalSumMatrix[row][col]
            minimalSumMatrix[m][n] = v+pv
        if m == 0 and n == 0:
            minimalSumMatrix[m][n] = matrix[0][0]

nodeMatrix = []
for row in range(M):
    temp =[]
    for col in range(N):
        temp.append(node((row,col)))
    nodeMatrix.append(temp)

def update():
    for row in range(M):
        for col in range(N):
            a = nodeMatrix[row][col]
            a.value()
    return minimalSumMatrix

def isIdentical(list1,list2):
    for row in range(M):
        for col in range(N):
            if list1[row][col] != list2[row][col]:
                return False
    return True

def main():
    initial = copy.deepcopy(minimalSumMatrix)
    next = copy.deepcopy(update())
    k = 0
    while not isIdentical(initial,next):
        k += 1
        printMatrix(minimalSumMatrix)
        print('\n')
        initial, next = next, update()
    printMatrix(minimalSumMatrix)
    print(minimalSumMatrix[M-1][N-1])

    route = []
    for row in range(M):
        temp = []
        for col in range(N):
            temp.append('*')
        route.append(temp)

    fm, fn = M-1, N-1
    sum_list = [matrix[fm][fn]]
    route[fm][fn] = '@'
    while fm != 0 or fn != 0:
        a = nodeMatrix[fm][fn].previousNode()
        print(a)
        fm, fn = a
        route[fm][fn] = '@'
        sum_list.append(matrix[fm][fn])

    for line in route:
        for h in line:
            print(h,end='')
        print('\r')

    print(sum(sum_list))
