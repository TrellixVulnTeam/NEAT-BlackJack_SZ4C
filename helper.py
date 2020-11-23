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


def update_graph(hall_of_fame, ao10, threshold_line, gen):
    style.use('fivethirtyeight')

    plt.plot(hall_of_fame, 'g-', label="Best")
    plt.plot(ao10, 'b--', label="Average of 10")
    plt.plot(threshold_line, 'r-', label="Goal")

    plt.title("NEAT Learning BlackJack -- Gen: %s" % gen)
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.legend()

    width = C_MIN_GRAPH_WIDTH if len(hall_of_fame) - 1 < C_MIN_GRAPH_WIDTH else len(hall_of_fame) - 1
    plt.axis([0, width, -C_FITNESS_THRESHOLD, C_FITNESS_THRESHOLD * 1.5])

    plt.draw()
    plt.pause(0.0001)
    plt.clf()
