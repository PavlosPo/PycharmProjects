import pandas
import engine
import datetime
import openpyxl
import random

NUM_OF_NUMBERS = 4  # HOW MANY NUMBERS YOU WANT TO RANDOMLY GENERATE AS LUCKY ONES ?
lucky_numbers = 0
file_name = 'kino_2021_09.xlsx'

data = pandas.read_excel(f'{file_name}', skiprows=[0, 1], usecols=[i for i in range(0, 23)])

data_columns_list = data.columns
# print(data_columns_list)
list_of_tupples = []
bingo_list = []


def make_list_of_data():
    for index , rows in data.iterrows():
        new_tupple = tuple(rows)
        list_of_tupples.append(new_tupple)


def search_the_data():
    for current_tuple in list_of_tupples:
        if set(lucky_numbers).issubset(current_tuple[2:]):  # dont search in current_tuple[0] cauz its the numbers of
            # playing ticket. Not the lucky numbers
            bingo_list.append(current_tuple)


def check(x1 , x2):
    # If algorithm
    if (x2 > 66) and x2 > x1 and x1 > 66:
        # If the last 3 days are the same day , better algorithm ?\

        return True
    elif x1 > x2:
        return False


def clear_the_last_loop_data():
    list_of_tupples.clear()
    bingo_list.clear()  # List with wining tickets




# random_lucky_numbers = engine.KinoEngine(15)  # A class I Made
# lucky_numbers = random_lucky_numbers.return_tupple(NUM_OF_NUMBERS)

loop_is_on = True
while loop_is_on:
    # Clear's the data from the previous loop
    clear_the_last_loop_data()

    # If it's the default value or not for lucky numbers

      # A class I Made
    lucky_numbers = engine.KinoEngine(40).return_tupple(NUM_OF_NUMBERS)

    make_list_of_data()
    search_the_data()
    n1 = abs(int(bingo_list[2][0]) - int(bingo_list[1][0]))
    n2 = abs(int(bingo_list[1][0]) - int(bingo_list[0][0]))

    # Check the algorithm _ Basic Version
    lucky_ticket = (n1 + n2) / 2 + int(bingo_list[0][0])
    if check(n1 , n2) and lucky_ticket < 900453:
        text_to_show_up = ''.join([f'{item} Lucky Numbers: {lucky_numbers}\n' for item in bingo_list[:20]])
        print(f'\nFound: n1={n1} , n2={n2}\n' ,
              f'Θελουμε την καθυστερηση: A = ( n1 + n2 ) / 2 = {(n1 + n2) / 2} \n Αρα '
              f'{bingo_list[0][0]} + A = {(n1 + n2) / 2 + int(bingo_list[0][0])}\n'
              , text_to_show_up)
        loop_is_on = False
    else:
        print('Ακυρο Δελτιο' , f' Unlucky Numbers:{lucky_numbers}')
        print('Next Loop')

    # text_to_show_up = ''.join([f'{item} Lucky Numbers: {lucky_numbers}\n' for item in bingo_list[:20]])
    # print(f'\nFound: n1={n1} , n2={n2}\n' , text_to_show_up)
