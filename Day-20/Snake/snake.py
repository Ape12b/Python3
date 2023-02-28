from turtle import Turtle


class Snake:
    def __init__(self, starting_position, speed):
        self.starting_position = starting_position
        self.snake_size = 3
        self.speed = speed
        self.snake = []
        self.initial_position()
        self.snake_head = self.snake[0]

    def initial_position(self):
        for i in range(self.snake_size):
            position = [-i * 20 + self.starting_position[0], self.starting_position[1]]
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.penup()
        tim.shape('square')
        tim.shapesize(1)
        tim.color('white')
        tim.goto(position)
        self.snake.append(tim)

    def extend_snake(self):
        self.add_segment(self.snake[-1].pos())

    def move(self):
        for seg in range(len(self.snake) - 1, -1, -1):
            if seg != 0:
                self.snake[seg].setposition(self.snake[seg - 1].pos())
            else:
                self.snake[seg].fd(self.speed)

    def up(self):
        if self.snake_head.heading() != 90 and self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90 and self.snake_head.heading() != 270:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0 and self.snake_head.heading() != 180:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 0 and self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def eating(self, food):
        if self.snake_head.distance(food) < 15:
            return True

    def detect_collision(self):
        if abs(self.snake_head.pos()[0]) > 300 or abs(self.snake_head.pos()[1]) > 300:
            return True
        else:
            for seg in range(1, len(self.snake)):
                if self.snake_head.distance(self.snake[seg]) < 5:
                    return True
        return False

    def snake_reset(self):
        for seg in self.snake:
            seg.hideturtle()
        self.snake = []
        self.initial_position()
        self.snake_head = self.snake[0]
