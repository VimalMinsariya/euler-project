import math

# 완전제곱수를 확인하는 함수
def isSquare(n):
    test = math.sqrt(n)
    if test == int(test):
        return True
    else:
        return False

# i^2 + N^2 이 제곱수인 경우(최단거리가 정수가 되는 경우)
# 최대 모서리의 길이가 N이고 나머지 두 모서리의 길이의 합이 i인 직육면체의 갯수를 구하는 함수.
def g(i,N):
    if i >= 2 and i <= 2*N:
        if i < N+2:
            result = i//2
        else:
            result = (2*N - i)//2 + 1
    else:
        result = 0
    return result

# 최대 모서리의 길이가 N이고, 문제의 최단경로의 길이가 정수인 직육면체의 갯수를 구하는 함수.
def f(N):
    result = 0
    for i in range(2,2*N+1):
        if isSquare(i**2 + N**2):
            result += g(i,N)
    return result

limit = 10**6
M = 1
total = f(M)
while total < limit:
    M += 1
    total += f(M)

print(M)