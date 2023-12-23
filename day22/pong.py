from turtle import Screen
from time import sleep
from platform import Platform
from ball import Ball
from scores import Score
from line import Line

screen = Screen()  # екран і звязане
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Platform((-370, 0))  # платформи створюю
player_2 = Platform((370, 0))

ball = Ball()
scores = Score()
line = Line()


screen.listen()  # керування платформами
screen.onkeypress(key="Up", fun=player_2.up)
screen.onkeypress(key="Down", fun=player_2.down)
screen.onkeypress(key="w", fun=player_1.up)
screen.onkeypress(key="s", fun=player_1.down)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.01)
    if ball.xcor() > 345 and ball.distance(player_2) < 50:  # провірка на зіткнення з платформою
        ball.direction_x = ball.m_speed * -1
    elif ball.xcor() < -345 and ball.distance(player_1) < 50:
        ball.direction_x = ball.m_speed
    ball.move()
    if ball.xcor() < -380:  # провірка на забиття гола
        scores.score_2 += 1
        scores.round()
        ball.round()
        sleep(1)
    elif ball.xcor() > 380:
        scores.score_1 += 1
        scores.round()
        ball.round()
        sleep(1)

screen.exitonclick()
