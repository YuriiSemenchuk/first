from turtle import Turtle


class Platform(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 6)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 6)
