from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()


pensize(5)
bgcolor('black')
hideturtle()

# green part
turtle_head(-120,60)
begin_fill()
color('green')
for x in range(2):
    forward(80)
    right(90)
    forward(120)
    right(90)
end_fill()

# white part
turtle_head(-40,60)
begin_fill()
color('white')
for x in range(2):
    forward(80)
    right(90)
    forward(120)
    right(90)
end_fill()

# red part
turtle_head(40,60)
begin_fill()
color('red')
for x in range(2):
    forward(80)
    right(90)
    forward(120)
    right(90)
end_fill()

exitonclick()