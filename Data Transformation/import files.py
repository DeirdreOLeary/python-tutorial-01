import pandas as pd
import numpy as np

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

# import csv data to a dataframe
colours_csv = '../sample-data/colors.csv'
colours_data = pd.read_csv(colours_csv, sep=',', na_values='[Unknown]')

print(colours_data.head())

print(type(colours_data))

# import Excel data (only 2nd & 3rd columns)
themes_xlsx = '../sample-data/themes.xlsx'
themes_df = pd.ExcelFile(themes_xlsx).parse(0, usecols=[1, 2])

print(themes_df.head())


## NUMPY ##

# import numeric data to array
num_file = '../sample-data/numbers.txt'
num_array = np.loadtxt(num_file, delimiter='\t', skiprows=1)

print(num_array)

# import mixed numeric & string data with headers (only 1st & 3rd columns)
mix_file = '../sample-data/mixed.txt'
mix_array = np.genfromtxt(mix_file, delimiter='\t',
                          names=True, dtype=None, usecols=[0, 2])

print(mix_array)
