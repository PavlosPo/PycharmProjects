# File Not Found
# with open('a_file.txt') as file:
#     file.read()


# KeyError
# a_dictionary = {'key':'value'}
# value = a_dictionary['non_existent_key']


# IndexError
# fruit_list = ['Apple','Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# To deal with those problems in real life programs
# we do the "Catching Exception" method. ( try except else finally )

# Lets catch the exception file not found
# try:
#     file = open('a_file.txt') # Will cause an error
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w') # 'w' method will open , if not exist it will create it.
#     file.write('Something')
# except KeyError as error_message: # we get hold the error message
#     print(f'That key {error_message} does not exists')
# else: # If try succed , then else block will execute
#     content = file.read()
#     print(content)
# finally: # It executes every time, no matter what happened before.
#     raise TypeError('This is an error that I made up')


height = float(input('Height: '))
weight = int(input('Weight: '))
if height > 3:
    raise ValueError('Human Height Should Not Be Over 3 Meters')


bmi = weight / height ** 2
print(bmi)