import neat
from matplotlib import style
import matplotlib.pyplot as plt

from config import C_HANDS_PER_GENERATION, C_FITNESS_THRESHOLD, C_MIN_GRAPH_WIDTH
from tabulate import tabulate


def display_game_results(player, dealer, game_number, message):
    table = [["Player", " ".join([c.label for c in player.hand]), player.score],
             ["Dealer", " ".join([c.label for c in dealer.hand]), dealer.score]]
    print("Game: %s (%s)" % (game_number + 1, message))
    print(tabulate(table, headers=["Player", "Hand", "Score"]) + "\n")


def display_sim_results(player):
    table = [[C_HANDS_PER_GENERATION,
              player.wins,
              (player.wins * 100 / C_HANDS_PER_GENERATION),
              (player.ties * 100 / C_HANDS_PER_GENERATION),
              (player.losses * 100 / C_HANDS_PER_GENERATION),
              ((player.wins + player.ties) * 100 / C_HANDS_PER_GENERATION)]]
    print(tabulate(table, headers=["Hands", "Wins", "Win %", "Tie %", "Loss %", "Win/Tie %"]) + "\n")


def deal_two_each(players, deck):
    # Deal two cards to each
    for player in players:
        player.hand.append(deck.top_card())

    deck.burn_top()

    for player in players:
        player.hand.append(deck.top_card())
        player.calc_score()

    deck.burn_top()

    return players, deck


def network(g, config):
    return neat.nn.FeedForwardNetwork.create(g, config)


def reward_genomes_for_wins(players, dealer, ge):
    msg = ''
    for j, player in enumerate(players):
        # Who won? Set message and counts
        if dealer.score < player.score <= 21 or player.score <= 21 < dealer.score:
            msg = "win"
            player.wins += 1
            ge[j].fitness += 10
            if player.score == 21:
                ge[j].fitness += 10
        elif player.score < dealer.score <= 21 or dealer.score <= 21 < player.score:
            msg = "loss"
            player.losses += 1
            ge[j].fitness -= 10
        else:
            msg = "tie"
            player.ties += 1

    return players, ge, msg


def average(hall_of_fame):
    if len(hall_of_fame) < 11:
        return round(sum(hall_of_fame) / len(hall_of_fame))
    else:
        return round(sum(hall_of_fame[-10:]) / 10)


def bottom_margin(num):
    if num > 0:
        return round(num / 9.0)
    else:
        return round(num * 1.1)
