from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score_1 = 0
        self.score_2 = 0
        self.round()

    def round(self):  # оновлюю рахунок
        self.clear()
        self.write(f"{self.score_1} : {self.score_2}", align=ALIGN, font=FONT)
