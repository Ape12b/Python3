from turtle import Turtle


class AllState:
    def __init__(self):
        self.states = []

    def add_state(self, state_name, x, y):
        if state_name not in self.states:
            tim = Turtle()
            tim.hideturtle()
            tim.color("Black")
            tim.penup()
            tim.setx(x)
            tim.sety(y)
            tim.write(state_name, True, align="center")
            self.states.append(state_name)

    def report(self):
        tim = Turtle()
        tim.hideturtle()
        tim.color("Black")
        tim.penup()
        tim.setx(50)
        tim.sety(300)
        if len(self.states) < 50:
            tim.write(f"You got {len(self.states)} out of 50 states.", True, align="center")
        else:
            tim.write(f"Hooray!! You got {len(self.states)} out of 50 states.", True, align="center")


