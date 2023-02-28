from turtle import Turtle


class Grid(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")

    def create_grid(self):
        self.penup()
        self.goto(-75, 25)
        self.pendown()
        self.goto(75, 25)
        self.penup()
        self.goto(-75, -25)
        self.pendown()
        self.goto(75, -25)
        self.penup()
        self.goto(-25, 75)
        self.pendown()
        self.goto(-25, -75)
        self.penup()
        self.goto(25, -75)
        self.pendown()
        self.goto(25, 75)
        self.penup()
