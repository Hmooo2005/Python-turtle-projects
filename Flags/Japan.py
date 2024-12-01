from turtle import *


def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
bgcolor('black')
hideturtle()

# white squre
turtle_head(-120,70)
begin_fill()
color("white")
for x in range(2):
    forward(240)
    right(90)
    forward(140)
    right(90)
end_fill()

# red circule
turtle_head(0,-50)
begin_fill()
color('red')
circle(50)
end_fill()
exitonclick()
