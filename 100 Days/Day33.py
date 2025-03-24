# Write data to a text file.

# Overwrite
with open('../sample-data/test2.txt', 'w') as file:
    file.write(f'Data overwritten on Mar 24 2025 @ 12:12')

# Append
with open('../sample-data/test2.txt', 'a') as file:
    file.write(f'\nData appended on Mar 24 2025 @ 12:14')