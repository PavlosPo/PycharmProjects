from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.initial_state()

    def go_up(self):
        self.forward(15)

    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def initial_state(self):
        self.goto(STARTING_POSITION)

