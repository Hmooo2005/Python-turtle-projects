from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
bgcolor('black')
hideturtle()

# blue part
turtle_head(-120,60)
begin_fill()
color('blue')
for x in range(2):
    forward(240)
    right(90)
    forward(120)
    right(90)
end_fill()

# yellow part
turtle_head(-120,0)
begin_fill()
color('yellow')
for x in range(2):
    forward(240)
    right(90)
    forward(60)
    right(90)
end_fill()
exitonclick()