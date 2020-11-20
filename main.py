from random import random

from Classes.Deck import Deck
from Classes.Player import Player
from config import C_HANDS_PER_GENERATION, C_BET_SIZE, C_STARTING_MONEY


def main():
    money = C_STARTING_MONEY

    for i in range(C_HANDS_PER_GENERATION):
        player = Player()
        dealer = Player()

        deck = Deck()

        deck.deal_to(player)
        deck.deal_to(dealer)
        deck.deal_to(player)
        deck.deal_to(dealer)

        while player.score < 17:
            if random() > 0.1:
                player.hit(deck)
            else:
                break

        while dealer.score < 17:
            dealer.hit(deck)

        print(player.score > dealer.score)

        if player.score > dealer.score:
            result = C_BET_SIZE
        elif player.score < dealer.score:
            result = -C_BET_SIZE
        else:
            result = 0

        money += result

    print("$%s" % money)


main()
