from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 2
TEST = False

data = loadDay(DAY, TEST)

answer = 0
for raw_line in data:
    line = raw_line.strip('\n\r')
    
    # split the line into rounds
    rounds = line.split(';')
    
    # Create a dictionary of the minimum number of each color to make the round possible
    min_color = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for round in rounds:

        # split the round by spaces
        words = round.split()

        # If the first word is "Game", then the round is the first one in the game
        if words[0] == "Game":
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

            # If the number is greater than the current minimum number of that color, then update the minimum number
            if number > min_color[color]:
                min_color[color] = number
    
    # Add the "power" of the round (the product of the minimum numbers) to the answer
    answer += min_color['red'] * min_color['green'] * min_color['blue']
    print(min_color)
    print(answer)

# print the answer
print(answer)
