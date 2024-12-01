from turtle import *
from function import turtle_head

pensize(5)
hideturtle()

# black part
turtle_head(-120,60) 
begin_fill()
color('black')
right(90)
forward(120) #1
left(90)   
forward(80)  #2
left(90)   
forward(120) #3
left(90)
forward(80)
end_fill()

# yellow part
turtle_head(-40,60) 
begin_fill()
color('yellow')
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