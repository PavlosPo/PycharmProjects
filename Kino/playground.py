import pandas
import openpyxl

data = pandas.read_excel('kino_2021_07.xlsx', skiprows=[0, 1], usecols=[i for i in range(0, 23)])
print(data.iloc[:4])
