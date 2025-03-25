# Read and display the contents of a text file.

with open('../sample-data/test.txt', 'r') as file:
    print(file.read())