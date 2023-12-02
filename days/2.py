from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 2
TEST = False

data = loadDay(DAY, TEST)

max_color = {
    "red": 12,
    "green": 13,
    "blue": 14
}

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')
    
    rounds = line.split(';')

    possible = True
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

            if number > max_color[color]:
                possible = False
                print 
                break

    if possible:
        answer += id # type: ignore
    
print(answer)