from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 1
TEST = False

data = loadDay(DAY, TEST)

digits= ['0','1','2','3','4','5','6','7','8','9','zero','one','two','three','four','five','six','seven','eight','nine']

no_letters = []

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')
    no_letters.append('')
    for char in line:
        if char in digits:
            no_letters[-1] = no_letters[-1] + char

for thing in no_letters:
    num = int(thing[0] + thing[-1])
    answer += num

print(answer)