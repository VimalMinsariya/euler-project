from pyx import *

c = canvas.canvas()
for i in range(0,100,2):
    horizon = path.line(0,i/10,10,i/10)
    vertical = path.line(i/10, 0, i/10, 10)
    if i%10 == 0:
        width = style.linewidth(0.015)
    else:
        width = style.linewidth(0.009)
    c.stroke(horizon, [width])
    c.stroke(vertical, [width])

#c.writeEPSfile("path")
c.writePDFfile("/Users/yslee/Desktop/c.pdf")
#c.writeSVGfile("path")
