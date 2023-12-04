from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 4
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

games = []

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')

    groups = line.split('|')

    win = groups[0].split()
    win.pop(0)
    id = int(win.pop(0)[:-1])

    have = groups[1].split()

    games.append((win, have))

def getScore(id):
    cards = 0
    win, have = games[id]

    score = 0
    for num in have:
        if num in win:
            score += 1
    
    cards += score

    for i in range(score):
        cards += getScore(id + i + 1)

    return cards

for i, game in enumerate(games):
    print(i)
    answer += getScore(i)

answer += len(games)

print(answer)