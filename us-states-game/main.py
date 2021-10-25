import turtle
import pandas
from drawing_turtle import Draw
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

tim = Draw() # a turtle that draw

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
correct_states = []
game_is_on = True

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f'{len(correct_states)}/50 Guess the State', prompt='Whats another states name?').title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:

        x_cor = int(data[data['state'] == answer_state].x)
        y_cor = int(data[data['state'] == answer_state].y)
        tim.go_to_and_write(x=x_cor, y=y_cor, word=answer_state)
        correct_states.append(answer_state.title())

missing_values = [state.title() for state in all_states if state.title() not in correct_states  ]
new_Data = pandas.DataFrame(missing_values)
new_Data.to_csv('missing_states.csv')
df = pandas.DataFrame(missing_values, columns=['Missing States of U.S.'])
df.to_csv('missing_states.csv')