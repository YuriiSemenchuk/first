from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)
        self.write(f"score = {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"score = {self.score}",align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGN, font=("Courier", 40, "normal"))
