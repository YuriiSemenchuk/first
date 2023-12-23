from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.m_speed = 1
        self.direction_y = self.m_speed
        self.direction_x = self.m_speed
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

    def move(self):
        if self.ycor() > 280:  # провіряю на зіткнення з стінкою
            self.m_speed += 0.2
            self.direction_y = self.m_speed * -1
        elif self.ycor() < -280:
            self.m_speed += 0.2
            self.direction_y = self.m_speed
        self.goto(self.xcor() + self.direction_x, self.ycor() + self.direction_y)

    def round(self):  # починаю наступний раунд
        self.m_speed = 1
        directories = [self.m_speed, -1 * self.m_speed]
        self.goto(0, 0)
        self.direction_y *= random.choice(directories)
        self.direction_x *= random.choice(directories)
