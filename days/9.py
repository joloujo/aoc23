from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 9
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

def predict(data):
    diff = np.diff(data)
    if np.all(diff == 0):
        return data[-1]
    else:
        change = predict(diff)
        return data[-1] + change

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')

    numbers = [int(word) for word in line.split()]
    data = np.array(numbers)
    answer += predict(data)    
    
print(answer)