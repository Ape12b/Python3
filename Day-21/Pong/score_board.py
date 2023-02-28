from turtle import Turtle


class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.initial_position(player)
        self.show_score()
        self.player_number = player.player_number

    def initial_position(self, player):
        if player.player_number == 1:
            self.setposition((-40, 220))
        else:
            self.setposition((40, 220))

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"{self.score}", move=False, align='center', font=('Courier', 50, 'normal'))

    def final_score(self, score):
        if self.score > score.score:
            self.home()
            self.write(f"Player {self.player_number} wins!! Final score {self.score}:{score.score}", move=False,
                       align='center', font=('Arial', 20, 'normal'))
        elif self.score < score.score:
            self.home()
            self.write(f"Player {score.player_number} wins!! Final score {self.score}:{score.score}", move=False,
                       align='center', font=('Arial', 20, 'normal'))
        else:
            self.home()
            self.write(f"Match Draw! Final score {self.score}:{score.score}", move=False,
                       align='center', font=('Courier', 20, 'normal'))