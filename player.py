import judgement_server as svr
from util import *

class Player(object):
    def __init__(self, id, client, name=None):
        if name == None:
            name = "Player " + str(id)
        self.name = name
        self.id = id
        self.client = client
        self.hand = []
        self.bid = 0
        self.tricks = []

    def getHandString(self):
        return ', '.join([str(card) for card in self.hand])

    def getTricksWon(self):
        return len(self.tricks)

    def addCard(self, card):
        self.hand.append(card)

    def sendMsg(self, *msg):
        msg = DATA_SEP.join(msg) + MSG_SEP
        self.client.send(msg.encode())
    
    def rcvSingleMsg(self):
        self.client.setblocking(1)
        msg = ""
        while True:
            try:
                msg += client.recv(MSG_LEN).decode("UTF-8")
                msgs = msg.split(MSG_SEP) 
                if (len(msgs) > 1): #if we have at least one complete command
                    return msgs[0]

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
