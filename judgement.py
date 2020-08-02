from card_class import *
from scoresheet import *
from player import *
from trick import *

class Judgement(object):
    def __init__(self):
        self.scores = ScoreSheet()
        self.Players = []
        self.currTrick = Trick()
        self.deck = Deck()
        self.num_cards = 52 // len(self.Players)
        # self.
    
    def deal(self):
        for c in range(self.num_cards):
            for p in self.Players:
                # TODO cross-check with player class
                p.addCard(self.deck.dealCard())

    def play_round(self):
        start_player = 0
        for turn in range(self.num_cards):
            for p in range(start_player, start_player + len(self.Players) - 1):
                player = self.Players[p % len(self.Players)]
                # TODO wait for client to send info
                c = player.playCard()
 
                # TODO implement add method in trick class
                self.currTrick.add(player, c)

            # TODO implement get_highest method in trick class
            winning_player, player_ind, trick = self.currTrick.get_highest()

            # TODO implement add_trick method in player class
            winning_player.add_trick(trick)
            start_player = player_ind

    def end_game(self):
        raise NotImplementedError
