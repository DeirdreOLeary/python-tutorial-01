# Append data to an existing text file.

with open('../sample-data/test2.txt', 'a') as file:
    file.write(f'\nData appended on Mar 24 2025 @ 12:14')
