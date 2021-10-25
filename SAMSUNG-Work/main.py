import pandas

# Ερωτημα 1
data = pandas.read_csv('data.csv')

# Ερωτημα 2
print('\nΕρωτημα 2\n',data.tail(5))

# Ερωτημα 3

num_of_columns = len(data.columns)
str_of_columns = " ".join(data.columns.tolist())
print(f'\nΕρωτημα3\nΟ αριθμος των στηλων ειναι: {num_of_columns}', f'\nΚαι οι στηλες ειναι: {str_of_columns}')

# Ερωτημα 4
print('\nΕρωτημα 4', data.dtypes)


# Ερωτημα 5
print('\nερωτημα 5\n', data.isna().any() )

# Ερωτημα 6

print(f'\nΕρωτημα 6\nΥπαρχουν {len(data)} εγραφες.')


# Οδηγιες για τον καθαρισμο του dataset

# Ερωτημα 1
print('\nΕρωτημα 2.1\n')
data = data.dropna(subset=['Description', 'CustomerID'], how='any')
print(data)

# Ερωτημα 2
print('\nΕρωτημα 2.2\n')
to_delete_list = ['AMAZON FEE', 'Manual', 'SAMPLES', 'POSTAGE', 'PACKING CHARGE']
for index_num in data.index:
    if data.at[index_num, 'Description'] in to_delete_list:
        data.drop(index_num, inplace=True)
print(data)

# Ερωτημα 3
print('\nΕρωτημα 2.3\n')
print(data[data.Quantity < 0])
data.drop(data[data.Quantity < 0], inplace=True)
print(data.info)
