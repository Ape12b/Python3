from turtle import Turtle


class Bat(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.player_number = player_number
        self.set_pos()

    def set_pos(self):
        if self.player_number == 1:
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def up(self):
        self.goto(self.pos()[0], self.pos()[1] + 20)

    def down(self):
        self.goto(self.pos()[0], self.pos()[1] - 20)

    def miss(self, ball, score):
        if self.player_number == 1:
            if ball.pos()[0] < self.pos()[0]:
                score.update_score()
                return True
            else:
                return False
        elif self.player_number == 2:
            if ball.pos()[0] > self.pos()[0]:
                score.update_score()
                return True
            else:
                return False

