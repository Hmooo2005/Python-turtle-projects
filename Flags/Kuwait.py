from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()


pensize(5)
hideturtle()

# black triangle
turtle_head(-120,-60)
begin_fill()
color('black')
left(90)
forward(120)
right(127)    # tri
forward(70)
right(53)
forward(40)
right(56)    #       le
forward(67)
end_fill()

# green part
turtle_head(-120,60)
begin_fill()
color('green')
forward(240)
right(90)
forward(40)
right(90)
forward(182)
end_fill()

# red part
turtle_head(-120,-60)
begin_fill()
color('red')
forward(240)
left(90)
forward(40)
left(90)
forward(182)
end_fill()

exitonclick()