import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()  # створюю екран
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


def move():
    if player.move():  # якщо гравець дошов до кінця
        scoreboard.round()


screen.listen()
screen.onkey(fun=move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    car_manager.create_car()
    if car_manager.move_cars(player):  # машини рухаются і провіряють колізію з гравцем
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
