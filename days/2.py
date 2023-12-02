from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 2
TEST = False

data = loadDay(DAY, TEST)

# Create a dictionary of the maximum number of each color
max_color = {
    "red": 12,
    "green": 13,
    "blue": 14
}

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')
    
    # split the line into rounds
    rounds = line.split(';')

    # Create a boolean to check if any round is possible
    possible = True
    for round in rounds:

        # split the round by spaces
        words = round.split()

        # If the first word is "Game", then the round is the first one in the game
        if words[0] == "Game":
            # Get the id of the game
            id = int(words[1][0:-1])
            # print(id)

            # Remove the first two words ("Game" and the id) so that the rest of the words are the same as the other rounds
            words.pop(0)
            words.pop(0)

        # print("DEBUG words:", words)

        # For each pair of words,
        for i in range(0, int(len(words)/2)):
            number = int(words[2 * i]) # The number is the first word of the pair
            color = words[2 * i + 1] # The color is the second word of the pair

            # Remove the comma or semicolon from the color if it exists
            if ',' in color or ';' in color:
                color = color[0:-1]

            # If the number is greater than the maximum number of that color, then the round is not possible
            if number > max_color[color]:
                possible = False
                # print("DEBUG impossible id:", id)
                break # for efficiency

    if possible:
        answer += id # type: ignore
    
# print the answer
print(answer)
