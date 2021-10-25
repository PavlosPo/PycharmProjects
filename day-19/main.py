from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'purple','magenta']
all_turtles = []
position = -100

for turtle_color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=position)
    all_turtles.append(new_turtle)
    position += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for current_turtle in all_turtles:
        if current_turtle.xcor() > 230:
            is_race_on = False
            winning_color = current_turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} won !")
            else:
                print(f"You've lost! The {winning_color} won !")
        rand_distance = random.randint(1, 10)
        current_turtle.forward(rand_distance)


screen.exitonclick()

