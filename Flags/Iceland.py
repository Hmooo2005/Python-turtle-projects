from turtle import *


def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()

pensize(5)
bgcolor('black')
hideturtle()

# blue square
turtle_head(-130,70)
begin_fill()
color('blue')
for x in range(2):
    forward(260) #1 3
    right(90)
    forward(140) #2 4
    right(90)
end_fill()

# white part

turtle_head(-55,70)
begin_fill()
color('white')
forward(40) #1
right(90)
forward(50)  #2
left(90)
forward(145) #3
right(90)
forward(40)  #4
right(90)
forward(145) #5
left(90)
forward(50)  #6
right(90)
forward(40)  #7
right(90)
forward(50)  #8
left(90)
forward(75) #9
right(90)
forward(40) #10
right(90)
forward(75) #11
left(90)
forward(50) #12
right(90)
end_fill()

# red part
turtle_head(-45,70)
begin_fill()
color('red')
forward(20) #1
right(90)
forward(60)  #2
left(90)
forward(155) #3
right(90)
forward(20)  #4
right(90)
forward(155) #5
left(90)
forward(60)  #6
right(90)
forward(20)  #7
right(90)
forward(60)  #8
left(90)
forward(85) #9
right(90)
forward(20) #10
right(90)
forward(85) #11
left(90)
forward(60) #12
right(90)
end_fill()
exitonclick()