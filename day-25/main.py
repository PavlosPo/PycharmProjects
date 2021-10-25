import pandas
#
#data = pandas.read_csv('weather_data.csv')
#
#
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data['temp'].to_list()
#print(temp_list)
#
#print(data['temp'].max())


#print(data[data.day == 'Monday'])

#data[ data.temp == data.temp.max() ]
#monday = data[data.day == 'Monday']
#print(monday.temp*1.8 + 32 )


#data_dict = {
#    'students': ['Amy', 'James', 'Angela'],
#    'scores': [76, 56, 65]
#}

#data = pandas.DataFrame(data_dict)
#data.to_csv('new_data.csv')

data = pandas.read_csv('2018_squirrel_data.csv')

size_of_gray = len(data[data['Primary Fur Color'] == 'Gray'])
size_of_red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
size_of_black = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [size_of_gray, size_of_red, size_of_black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv('squirrel_count.csv')