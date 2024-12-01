from turtle import *

def turtle_head(xx,yy):
    penup()
    home()
    goto(xx,yy)
    pendown()


pensize(5)
hideturtle()

# blue part
turtle_head(-120,60) 
begin_fill()
color('blue')
right(90)
forward(120) #1
left(90)   
forward(80)  #2
left(90)   
forward(120) #3
left(90)
forward(80)
end_fill()

# white part
turtle_head(-40,60) 
begin_fill()
color('white')
right(90)
forward(120) #1
left(90)   
forward(80)  #2
left(90)   
forward(120) #3
left(90)
forward(80)
end_fill()

# red part
turtle_head(40,60)
begin_fill()
color('red')
right(90)
forward(120) #1
left(90)   
forward(80)  #2
left(90)   
forward(120) #3
left(90)
forward(80)
end_fill()

exitonclick()