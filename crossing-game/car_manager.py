from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 6


class CarManager:
    def __init__(self):
        self.list_of_cars = []
        self.car_speed = 5

    def generate_car(self):
        new_car = Turtle()
        new_car.speed(STARTING_MOVE_DISTANCE)
        new_car.shape('square')
        new_car.left(90)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.goto((320, random.randint(-250, 250)))
        self.list_of_cars.append(new_car)

    def move_cars(self):
        for i in range(len(self.list_of_cars)):
            current_car = self.list_of_cars[i]
            current_car.goto(current_car.xcor() - self.car_speed, current_car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


        pass
