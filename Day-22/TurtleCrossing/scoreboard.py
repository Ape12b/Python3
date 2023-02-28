from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-250, 250)
        self.score = 0
        self.show_score()

    def update_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Game Over! Your level: {self.score}", align='center', font=FONT)

