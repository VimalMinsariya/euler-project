import numpy as np
import matplotlib.pyplot as plt

R, r = 12.5, 1.75
plt.figure(figsize=(R+1, R+1))
res = 100
t = np.arange(0,50*R*np.pi,1/res)
def x(t):
    result = (R-r)*np.cos(t) + r*np.cos((R-r)/r*t)
    return result
def y(t):
    result = (R - r) * np.sin(t) - r * np.sin((R - r) / r * t)
    return result
x1, y1 = x(t), y(t)
plt.axis([-R-1, R+1, -R-1, R+1])
plt.plot(x1, y1, linewidth=0.5)
plt.plot(R*np.cos(t),R*np.sin(t), linewidth =0.5)
plt.savefig('hypocloid.png', dpi=150)