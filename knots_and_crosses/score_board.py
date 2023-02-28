from turtle import Turtle


def show_toss_result(winner):
    tim = Turtle()
    tim.hideturtle()
    tim.sety(0)
    tim.setx(0)
    if winner == 1:
        tim.write("X goes first!")
    else:
        tim.write("O goes first!")


class Score(Turtle):
    def __init__(self, player1, player2):
        super().__init__()
        self.player1_name = player1.name
        self.player2_name = player2.name
        self.player1_score = player1.score
        self.player2_score = player2.score

    def show_score(self):
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.sety(250)
        tim.setx(-200)
        tim.write(f"{self.player1_name} : {self.player1_score}")

        tim.sety(250)
        tim.setx(200)
        tim.write(f"{self.player2_name} : {self.player2_score}")

    def show_winner(self, winner):
        tim = Turtle()
        tim.hideturtle()
        tim.sety(0)
        tim.setx(0)
        if winner == 1:
            tim.write(f"{self.player1_name} wins!")
        else:
            tim.write(f"{self.player2_name} wins!")

