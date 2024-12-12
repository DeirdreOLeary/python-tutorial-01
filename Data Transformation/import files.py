## BASIC IMPORT ##

# read a text file
# note: the context for python execution is python-tutorial-01, not python-tutorial-01/Data Transformation where the script is saved.
with open('../sample-data/test.txt', 'r') as txt_file:
    print(txt_file.read())

# read text file line-by-line
with open('../sample-data/test.txt', 'r') as txt_file:
    print(txt_file.readline())
    print(txt_file.readline())

## PANDAS ##

# import csv data
import pandas as pd

colours_csv = '../sample-data/colors.csv'
colours_data = pd.read_csv(colours_csv, sep=',', na_values='[Unknown]')

colours_data.head()

print(type(colours_data))

# import Excel data (only 2nd & 3rd columns)
themes_xlsx = '../sample-data/themes.xlsx'
themes_df = pd.ExcelFile(themes_xlsx).parse(0, usecols=[1, 2])

themes_df.head()
