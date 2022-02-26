import turtle
from turtle import Turtle
import random
turtle.colormode(255)


colors = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123)]

turtle1 = Turtle()

turtle1.speed(150)
turtle1.hideturtle()
turtle1.penup()
turtle1.setheading(225)
turtle1.forward(300)
turtle1.setheading(0)
nums_of_dots = 100
dot_count = 0

for i in range(1, nums_of_dots +1 ):
    dot_count += 1
    turtle1.dot(20,random.choice(colors))
    turtle1.penup()
    turtle1.forward(50)
    if dot_count%10 == 0:
        turtle1.setheading(90)
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)

screen = turtle.Screen()
screen.exitonclick()