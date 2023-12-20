from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(3):
            square = Turtle(shape="square")
            square.penup()
            square.speed("fastest")
            square.color("white")
            square.goto(POSITIONS[i])
            self.segments.append(square)
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def eating(self):
        square = Turtle(shape="square")
        square.penup()
        square.goto(self.segments[-1].position())
        square.color("white")
        self.segments.append(square)
