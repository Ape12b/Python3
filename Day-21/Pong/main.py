from turtle import Screen
from decoration import Deco
from bat import Bat
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
net = Deco(height=600)

screen.tracer(0)
net.make_net()
player1 = Bat(1)
player2 = Bat(2)

score1 = Score(player1)
score2 = Score(player2)
ball = Ball()

screen.listen()
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    if player1.miss(ball, score2) or player2.miss(ball, score1):
        ball.reset()
    elif score1.score >= 10 or score2.score >= 10:
        game_is_on = False
        screen.clear()
        screen.bgcolor("black")
        score1.final_score(score2)
    else:
        ball.player_collision(player1, player2, score1, score2)
        ball.wall_collision()
        ball.move()

screen.exitonclick()
