# Calculate the average of numbers in a text file.

def file_avg(filename):

    # read contents of file into list as strings
    with open(filename, 'r') as file:
        numbers = file.read().split('\n')

    # convert list's contents to integers
    numbers = [float(number) for number in numbers]

    # calculate & return the average of the contents of the list
    return (sum(numbers) / len(numbers))


print(file_avg('../sample-data/numbers2.txt'))
