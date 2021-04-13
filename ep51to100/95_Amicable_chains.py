def chains():
    divisorSumList = dict()
    N = 10**6

    for i in range(1,N):
        divisorSumList[i] = 1

    for d in range(2,N):
        for n in range(2*d,N,d):
            divisorSumList[n] += d

    print('list created!')

    abb = divisorSumList

    for n in range(1,N):
        seen = []
        while n < N and abb[n] != -1:
            seen.append(n)
            abb[n], n = -1, abb[n]
        if n in seen:
            yield seen[seen.index(n):]

print(max(chains(), key=len))
