from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 1
TEST = False

data = loadDay(DAY, TEST)

# create a dictionary of the digits to look for and their values
digits= {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# print("DEBUG digits keys:", digits.keys())

# create a list to store each line of the data file with no letters
no_letters = []

answer = 0 # start the sum for the answer at 0
for raw_line in data:
    line = raw_line # .strip('\n\r')

    # make lists for the first and last occurences of each digit
    indexes_list = []
    rindexes_list = []

    # find the first and last occurences of each digit
    for digit in digits.keys():
        indexes_list.append(line.find(digit))
        rindexes_list.append(line.rfind(digit))

    # find the first occurence of any digit
    indexes = np.array(indexes_list)
    if np.any(indexes == -1):
        indexes[indexes == -1] = 1000000
    first_index = np.argmin(indexes)

    # find the last occurence of any digit
    rindexes = np.array(rindexes_list)
    last_index = np.argmax(rindexes)

    # get the value of the first and last digits
    first_num = list(digits.values())[first_index] # type: ignore
    last_num = list(digits.values())[last_index] # type: ignore

    # print("DEBUG first and last number:", first_num, last_num)

    # create a two-digit number from the first and last digits and add it to the answer
    answer += first_num * 10 + last_num

# display the answer
print(answer)
