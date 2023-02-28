from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()


def forward():
    leo.fd(10)


def backward():
    leo.bk(10)


def turn_left():
    leo.left(2)


def turn_right():
    leo.right(2)


def clear():
    leo.clear()
    leo.penup()
    leo.home()
    leo.pendown()


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
