# twentyOne.py

import random

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank # from 0 to 12
        self.suit = suit # from 0 to 3

    def getString(self):
        rankString = 'A23456789TJQK'[self.rank]
        suitString = 'CDHS'[self.suit]
        return rankString + suitString

class Deck(object):
    def __init__(self):
        self.cards = [ ]
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def cardsLeft(self):
        return len(self.cards)

    def dealCard(self):
        return None if (self.cards == [ ]) else self.cards.pop()

class TwentyOne(object):
    def play(self):
        self.handsWon = 0
        self.handsPlayed = 0
        self.deck = Deck()
        self.printWelcomeMessage()
        while True:
            self.playTurn()
            if (not self.askYesOrNo('Keep playing?')):
                break
        self.printGoodbyeMessage()

    def printWelcomeMessage(self):
        print('''
Welcome to 21!
Get as close as you can to 21 without busting (going over).
Aces count as 1 or 11, whichever is better.
Face cards count as 10.
The dealer must hit (take a card) until 16, and stay on 17 or higher.
The dealer wins all ties.
Good luck!
''')

    def printGoodbyeMessage(self):
        print(f'Final score: {self.handsWon} out of {self.handsPlayed} hands.')
        print('Goodbye!')

    def playTurn(self):
        print(f'You have won {self.handsWon} out of {self.handsPlayed} hands.')
        self.handsPlayed += 1
        if (self.deck.cardsLeft() < 18):
            print('\n*** New Deck! ***\n')
            self.deck = Deck()
        playerScore = self.playPlayersHand()
        if (playerScore <= 21):
            dealerScore = self.playDealersHand()
            if ((dealerScore > 21) or (playerScore > dealerScore)):
                print('You win!')
                self.handsWon += 1
            else:
                print('Dealer wins!')

    def getHandString(self, hand):
        return ', '.join([card.getString() for card in hand])

    def getHandScore(self, hand):
        score = 0
        hasAce = False
        for card in hand:
            cardScore = min(card.rank + 1, 10)
            if (cardScore == 1):
                hasAce = True
            score += cardScore
        if (score <= 11) and hasAce:
            score += 10
        return score

    def playPlayersHand(self):
        print('Your turn!')
        hand = [ self.deck.dealCard() ]
        while True: 
            hand += [ self.deck.dealCard() ]
            print(f'Your hand: {self.getHandString(hand)}')
            score = self.getHandScore(hand)
            if (score > 21):
                print(f'Oh no, you busted with {score}!')
                break
            if (not self.askYesOrNo('Take another card (hit)?')):
                break
        print(f'Your score: {score}')
        return score

    def playDealersHand(self):
        print('Dealer turn!')
        hand = [ self.deck.dealCard() ]
        while True:
            hand += [ self.deck.dealCard() ]
            print(f'Dealer hand: {self.getHandString(hand)}')
            score = self.getHandScore(hand)
            if (score > 21):
                print(f'Oh no, Dealer busted with {score}!')
                break
            if (score >= 17):
                break
        print(f'Dealer score: {score}')
        return score

    def askYesOrNo(self, prompt):
        while True:
            result = input(prompt + ' [y]es or [n]o --> ').lower()
            if (result == 'y'): return True
            elif (result == 'n'): return False
            else: print('Please enter y or n!')

game = TwentyOne()
game.play()