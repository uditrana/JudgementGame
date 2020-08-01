# twentyOne.py

import random
from enum import Enum

class Suit(Enum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUBS = 3

class Rank(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN =10
    KING = 11
    ACE = 12

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank # from 0 to 12
        self.suit = suit # from 0 to 3

    def __str__(self):
        rankString = '23456789TJQKA'[self.rank.value]
        suitString = 'SHDC'[self.suit.value]
        return rankString + suitString

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def cardsLeft(self):
        return len(self.cards)

    def dealCard(self):
        return None if (self.cards == [ ]) else self.cards.pop()

d = Deck()
print(list(map(str, d.cards)))
cards = sorted(d.cards)
print(list(map(str, cards)))
