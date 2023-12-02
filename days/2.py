from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 2
TEST = True

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')
    

print(answer)