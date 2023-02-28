from turtle import Turtle


class Deco(Turtle):
    def __init__(self, height):
        super().__init__()
        self.height = height
        self.seg_height = 40
        self.net = []

    def make_net(self):
        for i in range(-int(self.height/self.seg_height/2), int(self.height/self.seg_height/2)+1):
            tim = Turtle()
            tim.shape("square")
            tim.shapesize(stretch_len=0.2, stretch_wid=self.seg_height/25)
            tim.penup()
            tim.color('white')
            tim.goto((0, self.seg_height*i))
            tim.speed('fastest')
            self.net.append(tim)

    def clear_net(self):
        for seg in self.net:
            seg.clear()

