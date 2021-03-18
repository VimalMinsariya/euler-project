import turtle
import sys
print(sys.version) #한글은 문제 없지요
turtle.setworldcoordinates(0,-2560,2560,0)
bob = turtle.Turtle()
bob.speed(0)
turtle.colormode(255)
bob.right(90)
for r in range(255):
    bob.setposition(0,-r * 10)
    for g in range(255):
        bob.color(r,g,0)
        bob.setx(g*10)
        bob.begin_fill()
        for i in range(4):
            bob.forward(10)
            bob.right(90)
        bob.end_fill()
turtle.done()
