from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()


setup(600,400)
bgcolor('blue')
hideturtle()

# white cross
begin_fill()
color('white')
pensize(40)
turtle_head(-300,200)
right(33.5)
forward(750)
turtle_head(300,200)
right(146.5)
forward(750)
end_fill()

exitonclick()