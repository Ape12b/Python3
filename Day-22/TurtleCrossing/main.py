import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Racing")
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
car_manager1 = CarManager()
score1 = Scoreboard()
screen.listen()

screen.onkeypress(player1.move, "Up")

game_is_on = True
while game_is_on:
    car_manager1.make_cars()
    time.sleep(0.1)
    screen.update()
    car_manager1.move()

    if player1.level_up():
        car_manager1.level_up()
        score1.update_score()
        player1.reset_turtle()

    if player1.collide(car_manager1):
        car_manager1.game_over()

        score1.game_over()
        game_is_on = False

    car_manager1.remove_cars()

screen.exitonclick()
