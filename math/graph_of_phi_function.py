from matplotlib import pyplot as plt
import math

def phi(n):
    cnt = 0
    for k in range(1,n):
        if math.gcd(n,k) == 1:
            cnt += 1
    return cnt

N = 1000
n_range = []
phi_range = []
for i in range(1,N+1):
    n_range.append(i)
    phi_range.append(phi(i))

plt.rc('text', usetex=True)
plt.rc('font', family='NanumGothicOTF')
plt.rc('axes', unicode_minus=False)
plt.axis([0, 1000, 0, 1000])
plt.plot(n_range,phi_range,'bo', markersize=1)
plt.xlabel('$n$', fontsize=16)
plt.ylabel(r'$\varphi(n)$', fontsize=16)
plt.title('')
plt.show()