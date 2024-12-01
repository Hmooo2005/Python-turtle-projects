from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
hideturtle()
setup(600,400)
bgcolor('#01411C')
speed(0)

# white rectangle
turtle_head(-300,200)
begin_fill()
color('white')
for x in range(2):
    forward(150)
    right(90)
    forward(400)
    right(90)
end_fill()

# white circule
turtle_head(75,-125)
begin_fill()
color('white')
circle(125)
end_fill()

#green circle
turtle_head(120,-80)
begin_fill()
color('#01411C')
circle(115)
end_fill()

# white star
turtle_head(120, 70)
color('white')
begin_fill()
for x in range(5):
    forward(90)
    left(144)
end_fill()

exitonclick()