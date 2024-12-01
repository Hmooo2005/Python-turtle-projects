from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
bgcolor('gray')
hideturtle()

# darkblue part
turtle_head(-125,75)
begin_fill()
color('darkblue')
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

# black part
turtle_head(-125,25)
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

# white part
turtle_head(-125,-25)
begin_fill()
color('white')
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

exitonclick()