# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

# TODO 1. Create a dictionary in this format:
with open('nato_phonetic_alphabet.csv') as file:
    nato_alphabet_data = pandas.read_csv(file)
    dict_data = {row.letter: row.code for index, row in nato_alphabet_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def result_without_errors():
    user_input_word = input('Enter word: ').upper()
    list_of_letters = [letter for letter in user_input_word]
    try:
        result = [dict_data[letter] for letter in user_input_word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        result_without_errors()
    else:
        print(result)