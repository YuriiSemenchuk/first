from turtle import Screen
from functions import move_forwards, move_bak, turn_left, turn_right, restart

screen = Screen()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_bak)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="c", fun=restart)
screen.exitonclick()
