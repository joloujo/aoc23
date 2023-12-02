from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 2
TEST = False

data = loadDay(DAY, TEST)

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')
    
    rounds = line.split(';')
    
    min_color = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for round in rounds:

        words = round.split()

        id: int
        if words[0] == "Game":
            id = int(words[1][0:-1])
            # print(id)

            words.pop(0)
            words.pop(0)

        # print(words)

        for i in range(0, int(len(words)/2)):
            number = int(words[2 * i])
            color = words[2 * i + 1]

            if ',' in color or ';' in color:
                color = color[0:-1]

            if number > min_color[color]:
                min_color[color] = number
    
    answer += min_color['red'] * min_color['green'] * min_color['blue']
    print(min_color)
    print(answer)

print(answer)