from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

screen.colormode(255)


def random_walk(turtle):
    import random
    turtle.pensize(20)
    turtle.speed(9)
    turtle.hideturtle()
    for _ in range(100):
        turtle.right(random.randint(0, 3)*90)
        turtle.forward(40)
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


def spirograph(turtle):
    import random
    turtle.speed(0)
    turtle.hideturtle()
    for _ in range(100):
        turtle.left(360/100)
        turtle.circle(100)
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))



# random_walk(leo)
spirograph(leo)
# for i in range(3, 11):
#     angle = ((i-2) * 180) / i
#     print(angle)
#     for _ in range(i):
#         leo.forward(100)
#         leo.right(180 - angle)
#



screen.exitonclick()