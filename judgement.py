from card_class import *
from scoresheet import *
from player import *

class Judgement(object):
    def __init__(self):
        self.scores = ScoreSheet()
        self.Players = []
        self.currTrick = []
        self.trick = []
        self.deck = Deck()
        self.num_cards = 52 // len(self.Players)
        # self.
    
    def deal(self):
        for p in self.Players:
            for c in range(self.num_cards):
                # TODO cross-check with player class
                p.addCard(self.deck.dealCard())

    def play(self):
        pass
        self.handsWon = 0
        self.handsPlayed = 0
        self.deck = Deck()
        self.printWelcomeMessage()
        while True:
            self.playTurn()
            if (not self.askYesOrNo('Keep playing?')):
                break
        self.printGoodbyeMessage()
