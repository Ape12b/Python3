from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(1)
        self.color('white')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def food_spawn(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

