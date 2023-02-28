from turtle import Turtle
import math
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 0.05
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.setheading(random.randint(235, 405))
        self.move()

    def move(self):
        self.fd(10)

    def cal_distance(self, player):
        if player.pos()[1] + 30 > self.pos()[1] > player.pos()[1] - 30:
            return abs(self.pos()[0] - player.pos()[0])
        elif player.pos()[1] + 30 < self.pos()[1]:
            return math.sqrt((self.pos()[0] - player.pos()[0]) ** 2 + (self.pos()[1] - (player.pos()[1] + 30)) ** 2)
        else:
            return math.sqrt((self.pos()[0] - player.pos()[0]) ** 2 + (self.pos()[1] - (player.pos()[1] - 30)) ** 2)

    def player_collision(self, player1, player2, score1, score2):
        if self.cal_distance(player1) < 20:
            self.player_strike(player1)
            self.ball_speed *= 0.9
        elif self.cal_distance(player2) < 20:
            self.player_strike(player2)
            self.ball_speed *= 0.9

    def wall_collision(self):
        if abs(self.pos()[1]) > 280:
            self.wall_strike()

    def player_strike(self, player):
        if player.player_number == 1:
            if self.heading() <= 180:
                self.setheading(180 - self.heading())

            else:
                self.setheading(360 + 180 - self.heading())

        else:
            if self.heading() > 270:
                self.setheading(360 + 180 - self.heading())
            else:
                self.setheading(180 - self.heading())

    def wall_strike(self):
        self.setheading(270 - self.heading() + 90)

    def reset(self):

        if self.xcor() > 0:
            self.setheading(random.randint(120, 240))
        else:
            self.setheading(random.randint(300, 420))
        self.goto(0, 0)
        self.move()
        self.ball_speed = 0.05


