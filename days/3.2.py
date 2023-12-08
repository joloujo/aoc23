from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 3
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

lines = data.readlines()

def get_adjacent_numbers(gear_x, gear_y):
    adjacent_numbers = []

    adjacent_to_gear = np.zeros((1, len(lines[0].strip())))[0]
    for x in [gear_x - 1, gear_x, gear_x + 1]:
        try:
            adjacent_to_gear[x] = 1
        except IndexError:
            continue

    for y in [gear_y - 1, gear_y, gear_y + 1]:
        try:
            raw_line = lines[y]
        except IndexError:
            continue

        line = raw_line.strip('\n\r') 

        number = 0
        linemask = np.zeros((1, len(line)))[0]
        for x, char in enumerate(line):
            if char.isdigit():
                number *= 10 
                number += int(char)
                linemask[x] = 1
            else:
                if np.any(np.logical_and(linemask, adjacent_to_gear)):
                    adjacent_numbers.append(number)

                number = 0
                linemask = np.zeros((1, len(line)))[0]
        
        if np.any(np.logical_and(linemask, adjacent_to_gear)):
            adjacent_numbers.append(number)
    
    return adjacent_numbers


answer = 0
for y, raw_line in enumerate(lines):
    line = raw_line.strip('\n\r')

    for x, char in enumerate(line):
        if char == "*":
            adjacent_numbers = get_adjacent_numbers(x, y)
            
            if len(adjacent_numbers) == 2:
                answer += adjacent_numbers[0] * adjacent_numbers[1]

print(answer)