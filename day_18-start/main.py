import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


tim.speed(100)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)) :
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

tim.pensize(1)
directions = [0, 90, 180, 270]
tim.speed(100)






screen = Screen()
screen.exitonclick()
