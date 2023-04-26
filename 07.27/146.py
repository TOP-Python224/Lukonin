from random import randrange
import pprint

NUMS_PER_LETTER = 15

card = {}
lower = 1
upper = 1 + NUMS_PER_LETTER

for letter in ["B", "I", "N", "G", "O"]:
    card[letter] = []
    while len(card[letter]) != 5:
        next_num = randrange(lower, upper)
        if next_num not in card[letter]:
            card[letter].append(next_num)
    lower = lower + NUMS_PER_LETTER
    upper = upper + NUMS_PER_LETTER

pprint.pprint(card)