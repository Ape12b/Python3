from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.game_score = 0
        self.high_score = 0
        self.hideturtle()
        self.color('white')
        self.setposition((0, 250))
        self.show_score()

    def update_score(self):
        self.game_score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.game_score}, High Score = {self.high_score}", False, align="center",
                   font=('Arial', 14, 'normal'))

    def update_high_score(self):
        if self.high_score < self.game_score:
            self.high_score = self.game_score
        self.game_score = 0
        self.show_score()

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER!", False, align="center", font=('Arial', 20, 'normal'))
