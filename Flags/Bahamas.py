from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

speed(0)
pensize(5)
bgcolor('gold')
hideturtle()
setup(600,400)


# deepskyblue part
turtle_head(-300,200)
begin_fill()
color('deepskyblue')
forward(600)
right(90)
forward(133.3)
right(90)
forward(455)
end_fill()

# deepskyblue part
turtle_head(-300,-200)
begin_fill()
color('deepskyblue')
forward(600)
left(90)
forward(133.3)
left(90)
forward(455)
end_fill()

# black triangle
turtle_head(-300,200)
begin_fill()
color('black')
right(43)    # tri
forward(300)  #    ang
right(96)    #       le
forward(300)
end_fill()

exitonclick()