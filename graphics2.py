#NONAGON SPIRAL

import turtle
#turtle.setposition(0,0)
turtle.speed(5)
n = 1
turtle.pencolor("pink")
while (n<=50):
    turtle.forward(n)
    turtle.left(40)
    n = n + 1


turtle.pencolor("violet")

while (n<=100):
    turtle.forward(n)
    turtle.left(40)
    n = n + 1
    
turtle.pencolor("blue")
while (n<=150):
    turtle.forward(n)
    turtle.left(40)
    n = n + 1


turtle.hideturtle()
turtle.update()
turtle.done()
