from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.color("black")
        self.level = 0
        self.round()

    def round(self):  # оновлюю рахунок
        self.clear()
        self.level += 1
        self.write(arg=f"level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game over", align="center", font=FONT)
