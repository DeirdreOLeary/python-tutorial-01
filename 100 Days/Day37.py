# Handle exceptions for file not found.

filepath = '../sample-data/ThisFileDoesNotExist.txt'

try:
    with open(filepath, 'r') as file:
        print(file.readline())

except:
    print('Error: File not found!')
