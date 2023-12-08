from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 6
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

answer = 1
lines = data.readlines()

# times = [int(word) for word in lines[0].split()[1:]]
# distances = [int(word) for word in lines[1].split()[1:]]

times = [35696887]
distances = [213116810861248]

for i, total_time in enumerate(times):
    count = 0
    for time in range(total_time):
        speed = time
        distance = speed * (total_time - time)
        if distance > distances[i]:
            count += 1
    
    print(count)
    answer *= count

print(answer)