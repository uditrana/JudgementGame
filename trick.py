from collections import OrderedDict

class Trick(object):
    def __init__(self, trumpSuit):
        self.cards = OrderedDict()
        self.trumpSuit = trumpSuit
        self.baseSuit = None
        self.highCard = None

    def newHighCard(self, card): # true if new card is higher than larger 
        assert(self.highCard != card)
        if self.highCard.suit == card.suit:
            return self.card.rank.value > self.highCard.rank.value
        elif card.suit == self.trumpSuit:
            return True
        else: return False

    def playCard(self, pid, card):
        if len(cards) == 0:
            self.cards[pid] = card
            self.baseSuit = card.suit
            self.highCard = card
        else:
            self.cards[pid] = card
            if self.newHighCard(card):
                self.highCard = card

    def finishTrick(self):
        for ind, (pid, card) in enumerate(self.cards):
            if card == self.highCard:
                return ind, cards, pid, self.highCard
