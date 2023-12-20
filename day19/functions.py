from turtle import Turtle

tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_bak():
    tim.forward(-10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def restart():
    tim.home()
    tim.clear()
