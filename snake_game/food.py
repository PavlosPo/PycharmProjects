from turtle import Turtle
import random

SHAPE = 'circle'
COLOR = 'blue'
SPEED = 'fastest'
SIZE_LENGTH = 0.5
SIZE_WIDTH = 0.5


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=SIZE_LENGTH, stretch_wid=SIZE_WIDTH)
        self.color(COLOR)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        random_x = (random.randint(-280 , 280))
        random_y = (random.randint(-280 , 280))
        self.goto(x=random_x , y=random_y)
