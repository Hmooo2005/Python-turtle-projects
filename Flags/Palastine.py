from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
hideturtle()

# red triangle
turtle_head(-120,-60)
begin_fill()
color('red')
left(90)
forward(120)
right(127)    # tri
forward(100)  #    ang
right(107)    #       le
forward(100)
end_fill()

# black part
turtle_head(-120,60)
begin_fill()
color('black')
forward(240)
right(90)
forward(40)
right(90)
forward(182)
end_fill()

# green part
turtle_head(-120,-60)
begin_fill()
color('green')
forward(240)
left(90)
forward(40)
left(90)
forward(182)
end_fill()

exitonclick()