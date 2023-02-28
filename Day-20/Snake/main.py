from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake game!!")
screen.tracer(0)

snake = Snake(starting_position=[0, 0], speed=20)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
food = Food()
score = Score()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if not snake.detect_collision():
        if snake.eating(food):
            food.food_spawn()
            snake.extend_snake()
            score.update_score()
    else:
        snake.snake_reset()
        score.update_high_score()
        temp = False
        with open("snake_score.txt", mode="r") as file:
            data = int(file.read())
            if data < score.high_score:
                temp = True
        if temp:
            with open("snake_score.txt", mode="w") as file:
                file.write(f"{score.high_score}")
screen.exitonclick()
