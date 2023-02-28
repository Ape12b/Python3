# TODO 1: Create the grid
# TODO 2: Create the toss
# TODO 3: Create the database to store and retrieve player information
# TODO 4: Create the player movement
# TODO 5: Create the game rules

import pandas
from toss import Toss
from turtle import Screen
from score_board import Score, show_toss_result
from grid_creator import Grid
import time
from player import Player

player_data = pandas.read_csv("player_data.csv", header=0)
player1_name = input("Please enter the player name: ")
player2_name = input("Please enter the player name: ")

player1 = Player(player1_name, player_data)
player_data = pandas.read_csv("player_data.csv")
player2 = Player(player2_name, player_data)

screen = Screen()
screen.setup(width=600, height=600)

toss_up = Toss()
choice = toss_up.throw_turtle()
screen.clear()
show_toss_result(choice)
time.sleep(2)

screen.clear()
grid = Grid()
grid.create_grid()
score = Score(player1, player2)
score.show_score()

screen.tracer()

screen.listen()
screen.onkeypress(player1.left(), "left")
screen.onkeypress(player1.right(), "right")
screen.onkeypress(player1.up(), "up")
screen.onkeypress(player1.down(), "down")
screen.onkeypress(player2.left(), "a")
screen.onkeypress(player2.right(), "d")
screen.onkeypress(player2.up(), "w")
screen.onkeypress(player2.down(), "s")
screen.onkeypress(player1.enter(), "enter")
screen.onkeypress(player2.enter(), "shift")

if choice == 1:
    while game_is_on:











screen.update()
screen.exitonclick()
