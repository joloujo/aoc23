from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 3
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

lines = data.readlines()

adjacent_to_symbol = np.zeros((len(lines), len(lines[0].strip())))

answer = 0
for y, raw_line in enumerate(lines):
    line = raw_line.strip('\n\r')

    for x, char in enumerate(line):
        if not char.isdigit() and char != ".":
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        adjacent_to_symbol[y+j, x+i] = 1
                    except IndexError:
                        pass

for y, raw_line in enumerate(lines):
    line = raw_line.strip('\n\r') 

    number = 0
    linemask = np.zeros((1, len(line)))[0]
    for x, char in enumerate(line):
        if char.isdigit():
            number *= 10 
            number += int(char)
            linemask[x] = 1
        else:
            if np.any(np.logical_and(linemask, adjacent_to_symbol[y])):
                answer += number

            number = 0
            linemask = np.zeros((1, len(line)))[0]
    
    if np.any(np.logical_and(linemask, adjacent_to_symbol[y])):
        answer += number

# for row in adjacent_to_symbol:
#     print("".join([str(int(elem)) for elem in row]))

print(answer)