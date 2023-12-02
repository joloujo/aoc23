from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 1
TEST = False

data = loadDay(DAY, TEST)

# create a list of the digits to look for
digits= ['0','1','2','3','4','5','6','7','8','9']

# create a list to store each line of the data file with no letters
no_letters = []

for raw_line in data:
    line = raw_line.strip('\n\r')

    # add an empty string to the no_letters list
    no_letters.append('')

    # add each character that is in the digits list to the last item in the no_letters list
    for char in line:
        if char in digits:
            no_letters[-1] = no_letters[-1] + char

answer = 0 # start the sum for the answer at 0
for char in no_letters:
    # concatenate the first and last digits to make the two-digit number
    num = int(char[0] + char[-1])

    # add the two-digit number to the answer
    answer += num

# display the answer
print(answer)
