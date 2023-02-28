from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.reset_turtle()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def collide(self, car_manager):
        for car in car_manager.cars:
            if abs(self.ycor() - car.ycor()) < 20:
                if self.distance(car) < 36:
                    return True
        return False

    def reset_turtle(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)
