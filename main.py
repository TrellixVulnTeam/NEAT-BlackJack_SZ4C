from Classes.Deck import Deck
from Classes.Player import Player
from config import C_HANDS_PER_GENERATION, C_BET_SIZE, C_STARTING_MONEY


def sim_game(player, dealer):
    deck = Deck()

    deck.deal_to(player)
    deck.deal_to(dealer)
    deck.deal_to(player)
    deck.deal_to(dealer)

    while player.score < 17:
        player.hit(deck)

    while dealer.score < 17:
        dealer.hit(deck)

    print(player.score > dealer.score)

    if player.score > dealer.score:
        return C_BET_SIZE
    elif player.score < dealer.score:
        return -C_BET_SIZE
    else:
        return 0


def main():
    hand_count = 0
    money = C_STARTING_MONEY
    while hand_count < C_HANDS_PER_GENERATION:
        hand_count += 1

        player = Player()
        dealer = Player()

        result = sim_game(player, dealer)
        money += result

    print("$%s" % money)


main()
