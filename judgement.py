from card_class import *
from scoresheet import *
from player import *

class Judgement(object):
    def __init__(self):
        self.scores = ScoreSheet()
        self.Players = []
        self.currTrick = []
    
    def deal(self):
        pass
        
        
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




