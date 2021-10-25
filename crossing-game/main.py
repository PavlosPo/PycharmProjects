import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars = CarManager()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, 'Up')

loop_count = 0
game_is_on = True
while game_is_on:
    loop_count += 1

    time.sleep(0.1)
    screen.update()

    # Generates new car in every 6th game loop
    if loop_count == 6:
        cars.generate_car()
        loop_count = 0

    # Detects collation with a car object
    for current_car in range(len(cars.list_of_cars)):
        if player.distance(cars.list_of_cars[current_car]) < 20 and abs(
                player.ycor() - cars.list_of_cars[current_car].ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()


    # Detects the finish Line
    if player.check_finish_line():
        cars.level_up()
        player.initial_state()
        scoreboard.update_score()

    cars.move_cars()
screen.exitonclick()