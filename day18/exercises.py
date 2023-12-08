from turtle import Turtle, Screen, colormode
from random import randint

timmy = Turtle()
timmy.color("green")
timmy.pencolor("black")
timmy.pensize(3)
colormode(255)


def ex1():
    timmy.shape("turtle")
    for i in range(4):
        timmy.forward(200)
        timmy.left(90)


def ex2():
    timmy.shape("arrow")
    for _ in range(50):
        timmy.pendown()
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)


def ex3():
    for i in range(3, 12):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        timmy.pencolor(r, g, b)
        angle = 360 / i
        lines = 0
        while lines != i:
            timmy.forward(100)
            timmy.right(angle)
            lines += 1
        timmy.home()


def ex4():
    timmy.speed(10)
    for _ in range(200):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        timmy.pencolor(r, g, b)
        timmy.pensize(5)
        timmy.right(90 * randint(0, 3))
        timmy.forward(30)


def ex5():
    timmy.speed("fastest")
    timmy.pensize(1)
    circles = 50
    for _ in range(circles):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        timmy.pencolor(r, g, b)
        timmy.circle(150)
        timmy.right(360 / circles)


ex5()
screen = Screen()
screen.exitonclick()
