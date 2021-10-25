import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(1000)
screen = Screen()

color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162),
              (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89),
              (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166),
              (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193),
              (166, 200, 213)]


def create_dot():
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.hideturtle()
    tim.setx(tim.xcor() + 50)


def change_row(number_of_yrow):
    tim.hideturtle()
    tim.penup()
    tim.setposition(-250, -1000)
    tim.sety(number_of_yrow * 50)


screen.screensize(100, 100)
for row in range(1, 11):
    change_row(row)
    for column in range(1, 11):
        create_dot()


screen.exitonclick()
