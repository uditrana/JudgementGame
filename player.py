class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.hand = []

    def getHandString(self):
        return ', '.join([card.getString() for card in self.hand])
