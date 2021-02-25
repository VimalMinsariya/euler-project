import turtle

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
        for i in range(4):  # 사각형이므로 4번 반복
            bob.forward(10)
            bob.right(90)
        bob.end_fill()

turtle.done()