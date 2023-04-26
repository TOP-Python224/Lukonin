from random import *


def gen_card():
    """Генерирует упорядоченную колоду из 52 карт."""
    for suit in ('черви', 'бубны', 'пики', 'крести'):
        for value in range(1, 14):
            yield value, suit


deck_card = gen_card()

print(deck_card.__next__())
print(deck_card.__next__())
print(deck_card.__next__())
print(deck_card.__next__())
print(deck_card.__next__())
print(deck_card.__next__(), end='\n\n')


def card_mixed():
    """Генерирует перемешанную колоду из карт"""
    cards = list(gen_card())
    for _ in range(52):
        card = choice(cards)
        cards.remove(card)
        yield card


gen_card_mixed = card_mixed()

print(gen_card_mixed.__next__())
print(gen_card_mixed.__next__())
print(gen_card_mixed.__next__())
print(gen_card_mixed.__next__())
