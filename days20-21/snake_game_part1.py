from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)   # включаю покадрову анімацію
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # керуваня змійкою
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()  # змінюю кадр
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:  # провіряю на зїдження їжі
        snake.extend()
        food.eaten()
        scoreboard.score += 1
        scoreboard.update_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # провіряю на зіткнення з стінами
        scoreboard.reset()
        snake.reset()
    for square in snake.segments[1:]:  # провіряю на зіткнення з тілом
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
