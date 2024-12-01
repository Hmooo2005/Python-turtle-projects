from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
hideturtle()

# black part
turtle_head(-125,75)
begin_fill()
color('black')
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

# red part
turtle_head(-125,25)
begin_fill()
color('red')
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

# yellow part
turtle_head(-125,-25)
begin_fill()
color('yellow')
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

exitonclick()