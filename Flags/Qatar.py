from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()


pensize(5)
bgcolor('black')

# red flag
turtle_head(-120,60)
begin_fill()
color('red')
for x in range(2):
    forward(240)
    right(90)
    forward(120)
    right(90)
end_fill()


# white part
turtle_head(-90,60)
begin_fill()
color('white')
right(40)
forward(15.620499351813308)
right(90)
forward(15.620499351813308)
left(135)
forward(15.620499351813308)
right(135)
forward(15.620499351813308)
# left(135)
# forward(15.620499351813308)
# right(135)
# forward(15.620499351813308)
# left(135)
# forward(15.620499351813308)
# right(135)
# forward(15.620499351813308)
# left(135)
# forward(15.620499351813308)
# right(135)
# forward(15.620499351813308)
# left(135)
end_fill()

exitonclick()