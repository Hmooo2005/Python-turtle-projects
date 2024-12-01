from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()


pensize(5)
bgcolor('black')
hideturtle()

# blue triangle
turtle_head(-120,-60)
begin_fill()
color('blue')
left(90)
forward(120)
right(127)    # tri
forward(100)  #    ang
right(107)    #       le
forward(100)
end_fill()

# white part
turtle_head(-120,60)
begin_fill()
color('white')
forward(240)
right(90)
forward(60)
right(90)
forward(155)
end_fill()

# red part
turtle_head(-120,-60)
begin_fill()
color('red')
forward(240)
left(90)
forward(60)
left(90)
forward(155)
end_fill()

exitonclick()