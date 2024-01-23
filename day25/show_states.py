from turtle import Turtle

class Show_states(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def show_state(self,name, x, y):
        x = int(x)
        y = int(y)
        self.goto(x, y)
        self.write(arg=name)
