from turtle import Screen, Turtle
import random
screen = Screen()
screen.setup(500, 400)
start = -200
finish = 200
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [20, 50, 80, -10, -40, -70]
for i in range(6):  # створюю черепах
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(y=positions[i], x=start)
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")
is_race_on = True
winner = None
while is_race_on:  # черепахи рухаются поки хтось не виграє
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > finish or turtle.xcor() == finish:
            is_race_on = False
            winner = turtle.pencolor()

if user_bet == winner:
    print(f"You are won! The winner is {winner}")
else:
    print(f"You are lost! The winner is {winner}")

screen.exitonclick()
