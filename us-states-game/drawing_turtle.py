from turtle import Turtle


class Draw(Turtle):

    def __init__(self):
        super(Draw, self).__init__()
        self.hideturtle()
        self.penup()

    def go_to_and_write(self, x, y, word):
        self.goto((x, y))
        self.write(f'{word.capitalize()}', align='center')

