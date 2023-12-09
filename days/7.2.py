from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 7
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

card_strength = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def get_type_rank(hand):

    if 'J' in hand:
        i = hand.index('J')
        highest_rank = 0
        for card in card_strength[1:]:
            new_hand_split = list(hand)
            new_hand_split[i] = card
            new_hand = "".join(new_hand_split)

            # print(new_hand)

            new_hand_rank = get_type_rank(new_hand)
            if new_hand_rank > highest_rank:
                highest_rank = new_hand_rank

        return highest_rank

    cards = dict()
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1  

    if len(list(cards.keys())) == 1:
        # 5 of a kind
        return 6
    elif len(list(cards.keys())) == 2:
        # 4 of a kind or full house
        for value in list(cards.keys()):
            if cards[value] == 4:
                # 4 of a kind
                return 5
        return 4
    elif len(list(cards.keys())) == 3:
        # 3 of a kind or 2 pair
        for value in list(cards.keys()):
            if cards[value] == 3:
                # 3 of a kind
                return 3
        # two pair
        return 2
    elif len(list(cards.keys())) == 4:
        return 1
    else:
        return 0

def hand_to_strength(hand):

    multiplier_step = 100
    multiplier = pow(multiplier_step, len(hand))

    strength = get_type_rank(hand) * multiplier
    multiplier /= multiplier_step

    for card in hand:
        strength += card_strength.index(card) * multiplier
        multiplier /= multiplier_step

    return strength

lines = data.readlines()


strengths_and_bids = [(hand_to_strength(line.strip('\n\r').split()[0]), int(line.strip('\n\r').split()[1])) for line in lines]
strengths_and_bids.sort(key=lambda x: x[0])
multiplied_bids = [sab[1] * (i+1) for i, sab in enumerate(strengths_and_bids)]

print(sum(multiplied_bids))