import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 0.5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 50)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_cars(self, player):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            if car.distance(player) < 20:
                return True
            if car.xcor() > 300:
                car.hideturtle()
                self.all_cars.remove(car)
