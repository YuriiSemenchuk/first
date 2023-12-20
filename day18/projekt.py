import random
from turtle import Turtle, Screen, colormode
timmy = Turtle()
timmy.color("black")
timmy.shape("arrow")
timmy.penup()
size = 30
colormode(255)
timmy.speed("fast")
x_start = -300
y_start = -300
y_position = -300
step = 60
dots_in_line = 10
timmy.setposition(x_start, y_start)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213),
              (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203)
              ]


for i in range(dots_in_line):
    timmy.setheading(0)
    timmy.dot(size, random.choice(color_list)) # роблю першу точку в лінії
    for _ in range(dots_in_line - 1):  # роблю лінію
        timmy.forward(step)
        timmy.dot(size, random.choice(color_list))
    # переходжу в нову лінію
    timmy.setheading(90)
    timmy.forward(step)
    timmy.setheading(180)
    y_position += step
    timmy.setx(x_start)
    timmy.setposition(x_start, y_position)
timmy.hideturtle()


screen = Screen()
screen.exitonclick()
