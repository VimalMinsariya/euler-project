import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(-10*np.pi,10*np.pi), ylim=(-2,2))
x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)

def rcolor(t):
    c = '#'
    for i in range(3):
        k = (int(t*100)+i*100)%256
        if k < 16:
            c += '0' + str(hex(k))[2:]
        else:
            c += str(hex(k))[2:]
    return c

curve, = ax.plot([], [])

def init():
    curve.set_data([], [])
    return curve,

def animate(t):
    y1 = np.add(t*np.sin(x), np.sin(1.1*x-2))
    curve.set_color(rcolor(t))
    curve.set_data(x,y1)
    return curve,

l1 = np.arange(-1,1,0.01)
l2 = np.arange(1,-1,-0.01)
l = np.concatenate((l1,l2))
ani = animation.FuncAnimation(fig, animate, init_func=init,\
    frames=l, interval=10, blit=True, repeat=True)

#f = r"/Users/yslee/Desktop/animation.mp4"
#writervideo = animation.FFMpegWriter(fps=60)
#ani.save(f, writer=writervideo)

plt.show()