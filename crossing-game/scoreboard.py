from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto((-250,250))
        self.level_score = 0
        self.update_score()

    def write_score(self):
        self.clear()
        self.write(self.write(f'Level: {self.level_score}', font=FONT, align='left'))

    def update_score(self):
        self.level_score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(self.write('GAME OVER', font=FONT, align='right'))
