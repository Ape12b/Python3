from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)

is_race_on = False
color_palate = ["blue", "red", "green", "yellow", "black"]
turtles = []

choice = screen.textinput(prompt="Which turtle will win? 'blue', 'red', 'green', 'yellow', 'black'", title="Quiz")

for i in range(5):
    temp_turtle = Turtle()
    temp_turtle.color(color_palate[i])
    temp_turtle.shape("turtle")
    turtles.append(temp_turtle)

for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].setposition(-240, (i - 2) * 50)

if choice is not None:
    is_race_on = True

while is_race_on:
    for i in turtles:
        i.fd(random.randint(0, 10))
        if i.position()[0] >= 250:
            winner = i.color()
            is_race_on = False
screen.exitonclick()
if winner[0].lower() == choice.lower():
    print(f"Hooray! your choice, {choice} turtle wins!")
else:
    print(f"Oops! your choice, {choice} turtle lost! The {winner[0]} turtle, won!")
