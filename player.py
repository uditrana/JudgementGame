import judgement_server as svr

class Player(object):
    def __init__(self, id, name=None):
        if name == None:
            name = "Player " + str(id)
        self.name = name
        self.id = id
        self.hand = []
        self.bid = 0
        self.tricks = []

    def getHandString(self):
        return ', '.join([str(card) for card in self.hand])

    def getTricksWon(self):
        return len(self.tricks)

    def addCard(self, card):
        self.hand.append(card)

    def getBid(self):
        # TODO communicate with client
        self.bid = 0
        return self.bid

    def playCard(self):
        # TODO communicate with client
        card_ind = 0
        return self.hand[card_ind]

    def addTrick(self, trick):
        self.tricks.append(trick)

    def won(self):
        return self.bid == len(self.tricks)
