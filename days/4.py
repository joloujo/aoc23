from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 4
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')

    groups = line.split('|')

    win = groups[0].split()
    win.pop(0)
    id = int(win.pop(0)[:-1])

    have = groups[1].split()

    score = 0
    for num in have:
        if num in win:
            print(num, "matches in", id)
            if score == 0:
                score = 1
            else: 
                score *= 2
    print(score)
    answer += score

print(answer)