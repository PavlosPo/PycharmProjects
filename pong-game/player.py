import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.super = Turtle()
        self.create_paddle()

    def create_paddle(self):
        turtle.resizemode('user')
        self.penup()
        self.shape('square')
        self.color('white')
        self.goto(self.coordinates)
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 25
        self.goto(self.coordinates[0], new_y)

    def move_down(self):
        new_y = self.ycor() - 25
        self.goto(self.coordinates[0], new_y)
