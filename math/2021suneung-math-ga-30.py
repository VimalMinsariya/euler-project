import numpy as np                       # 배열생성을 위한 numpy모듈 호출
from matplotlib import pyplot as plt     # 그래프 출력을 위한 pyplot 모듈 호출

a=0.4
b=0.2
c=0.2

def f(x):
    result = (x-a)**3 - b*(x-a) + c
    return result

def s(x):
    result = (np.sin(np.pi*x))**2
    return result

x = np.linspace(-0.2,1.2,600)        # x 좌표값 생성 (-pi ~ +pi)
y1 = [f(i) for i in x]          # y = cos(x) 계산
y2 = [f(s(i)) for i in x]

plt.plot(x,y1,label="y=f(x)")                            # 그래프에 x,y 입력
plt.legend()
plt.plot(x,y2,label="y=g(x)")
plt.legend()
plt.show()                               # 그래프 출력