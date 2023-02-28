from turtle import Turtle
import random
import math


class Toss(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-50, 0.1)
        self.pendown()
        self.throw_speeed = 50
        self.curr_x = -50
        self.curr_y = 0

    def throw_turtle(self):
        throw_angle = random.randint(60, 85)
        time = 0.1
        num_bounces = 3
        while num_bounces > 0:
            self.setx(self.curr_x + self.throw_speeed * time * math.cos(math.radians(throw_angle)))
            self.sety(self.curr_y + self.throw_speeed * time * math.sin(math.radians(throw_angle)) - 9.8 * time ** 2)
            time += 0.1
            if self.ycor() < 0:
                self.throw_speeed = self.throw_speeed / 1.2
                time = 0.1
                num_bounces -= 1
                self.curr_x = self.xcor()
                self.curr_y = 0.1
        return random.randint(1, 2)
