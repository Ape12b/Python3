import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.direction = 180
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.make_cars()

    def move(self):
        for car in self.cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def make_cars(self):
        if random.randint(0, 3) == 1:
            tim = Turtle()
            tim.shape('square')
            tim.setheading(self.direction)
            tim.shapesize(stretch_len=3, stretch_wid=1)
            tim.penup()
            tim.color(random.choice(COLORS))
            tim.goto(350, random.randint(-290, 270))
            self.cars.append(tim)

    def remove_cars(self):
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)

    def game_over(self):
        self.car_speed = 0