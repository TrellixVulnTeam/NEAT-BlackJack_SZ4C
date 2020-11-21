from random import shuffle

from Classes.Card import Card

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for i, label in enumerate(labels):
                self.cards.append(Card(label, suit, values[i]))
        shuffle(self.cards)

    def deal_to(self, player):
        card = self.cards.pop()
        if card.value == 1:
            player.has_ace = True
        player.hand.append(card)
        player.calc_score()

    def top_card(self):
        return self.cards[0]

    def burn_top(self):
        return self.cards.pop(0)

    def display(self):
        for card in self.cards:
            print(card.name)
