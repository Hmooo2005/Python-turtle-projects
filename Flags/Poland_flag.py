from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
bgcolor('black')
hideturtle()

# white part
turtle_head(-120,60)
begin_fill()
color('white')
forward(240)
right(90)
forward(60)
right(90)
forward(240)
right(90)
forward(60)
end_fill()

# red part
turtle_head(-120,0)
begin_fill()
color('red')
forward(240)
right(90)
forward(60)
right(90)
forward(240)
right(90)
forward(60)
end_fill()


exitonclick()