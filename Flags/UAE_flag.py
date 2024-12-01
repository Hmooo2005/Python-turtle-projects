from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
bgcolor('yellow')
hideturtle()

# red coloum part
turtle_head(-120,60)
begin_fill()
color('red')
forward(60)
right(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

# green part
turtle_head(-60,60)
begin_fill()
color('green')
forward(180)
right(90)
forward(40)
right(90)
forward(180)
right(90)
forward(40)
end_fill()

# white part
turtle_head(-60,20)
begin_fill()
color('white')
forward(180)
right(90)
forward(40)
right(90)
forward(180)
right(90)
forward(40)
end_fill()

# black part
turtle_head(-60,-20)
begin_fill()
color('black')
forward(180)
right(90)
forward(40)
right(90)
forward(180)
right(90)
forward(40)
end_fill()

exitonclick()