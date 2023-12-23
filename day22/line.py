from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 230)
        self.write("|", align=ALIGN, font=FONT)
        for _ in range(10):
            self.goto(0, self.ycor() - 50)
            self.write("|", align=ALIGN, font=FONT)
