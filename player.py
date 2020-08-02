class Player(object):
    def __init__(self, id, name=None):
        if name == None:
            name = "Player " + str(id)
        self.name = name
        self.id = id
        self.hand = []
        self.tricks = []

    def getHandString(self):
        return ', '.join([card.getString() for card in self.hand])

    def getTricksWon(self):
        return len(self.tricks)
