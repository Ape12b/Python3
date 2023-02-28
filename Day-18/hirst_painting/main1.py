import colorgram

colors = colorgram.extract("hirstImage.jfif", 30)

color_all = []
for i in colors:
    color_all.append((i.rgb[0], i.rgb[1], i.rgb[2]))

for _ in range(4):
    color_all.pop(0)
print(len(color_all))

import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.colormode(255)

tim.penup()
tim.right(90)
tim.fd(200)
tim.right(90)
tim.fd(200)
tim.left(90)
tim.left(90)
tim.pendown()
for _ in range(10):
    for _ in range(10):
        tim.dot(20, color_all[random.randint(0, len(color_all) - 1)])

        tim.penup()
        tim.fd(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.left(180)
    tim.pendown()

tim.hideturtle()

screen.exitonclick()
