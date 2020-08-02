from card_class import *
from collections import OrderedDict

from scoresheet import *
from player import *
from trick import *

class Judgement(object):
    def __init__(self):
        self.scores = ScoreSheet()
        self.Players = OrderedDict()
        self.currTrick = Trick()
        self.deck = Deck()
        self.num_cards = 52 // len(self.Players)

    def add_player(pid):
        p = Player(pid)
        self.Players[pid] = p
    
    def deal(self):
        for c in range(self.num_cards):
            for p in self.Players.values():
                p.addCard(self.deck.dealCard())

    def collect_bids(self):
        for ind, (pid, p) in enumerate(self.Players.items()):
            if ind == len(self.Players) - 1:
                invalid = self.num_cards - self.scores.getSumOfBids()
                bid = p.getBid(invalid = invalid)
            else:
                bid = p.getBid()

            self.scores.setBid(pid, bid)

    def play_round(self):
        start_player = 0
        for turn in range(self.num_cards):
            for p in range(start_player, start_player + len(self.Players)):
                pid, player = list(self.Players.items())[p % len(self.Players)]
                self.currTrick.playCard(pid, player.playCard())

            player_ind, trick, winning_pid, _ = self.currTrick.finishTrick()
            winning_player = self.Players[winning_pid]

            winning_player.addTrick(trick)
            start_player = player_ind
            self.currTrick = Trick()

        for pid, p in self.Players.items():
            self.scores.convertPlayerBidToScore(pid, p.won())

    def end_game(self):
        raise NotImplementedError
