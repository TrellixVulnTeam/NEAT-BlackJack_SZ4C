import os
import pickle
import neat

from Classes.Deck import Deck
from Classes.Graph import Graph
from Classes.Player import Player

from config import C_HANDS_PER_GENERATION, C_FITNESS_THRESHOLD, C_NEAT_CONFIG_DEFAULTS
from helper import display_game_results, display_sim_results, network, deal_two_each, reward_genomes_for_wins, average

# Globals to keep track of
G_gen = 0
G_hall_of_fame = [0]
G_ao10 = [0]


# What will evaluate our genomes
def eval_genomes(genomes, config):
    # Grab our globals
    global G_gen
    global G_hall_of_fame

    # Increment generation
    G_gen += 1

    # Make our empty lists of players, genomes, and N networks
    players = []
    nets = []
    ge = []

    # Set an impossibly low best fitness, so we can easily find our best of each generation
    best_fitness = -1000
    best_player = Player()

    # For each genome...
    for _, g in genomes:
        # Give them a starting fitness of 0
        g.fitness = 0

        # Add players, neural networks, and genomes to our own lists
        players.append(Player())
        nets.append(network(g, config))
        ge.append(g)

    # For every hand we want to play in a simulation...
    for i in range(C_HANDS_PER_GENERATION):
        # Let's use a new deck each time
        deck = Deck()
        dealer = Player()

        # Deal two cards to each player
        players, deck = deal_two_each(players, deck)

        for _ in range(2):
            deck.deal_to(dealer)

        for j, player in enumerate(players):
            d = Deck()
            d.cards = []
            for card in deck.cards:
                d.cards.append(card)

            # Activation function
            inputs = player.score, player.has_ace, dealer.hand[0].value
            output = nets[j].activate(inputs)

            # While we have less than 17 points, hit, except 10% of the time stay
            while output[0] > 0.5 and player.score < 21:
                player.hit(d)
                ge[j].fitness += 0.1

        # Standard dealer rules, hit on and up to 16
        while dealer.score <= 16:
            dealer.hit(deck)

        players, ge, msg = reward_genomes_for_wins(players, dealer, ge)

        for j, g in enumerate(ge):
            if g.fitness > best_fitness:
                best_fitness = g.fitness
                best_player = players[j]

        # Display the results of the final game
        if i + 1 == C_HANDS_PER_GENERATION:
            display_game_results(best_player, dealer, i, msg)

        # Make sure their hands are empty
        for player in players:
            player.clear_hand()
        dealer.clear_hand()

    # Display the results of the whole simulation
    display_sim_results(best_player)


def run(path):
    global G_gen
    global G_hall_of_fame

    config = neat.config.Config(*C_NEAT_CONFIG_DEFAULTS, path)
    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    best_fitness = -1000
    winner = neat.DefaultGenome(0)

    graph = Graph(C_FITNESS_THRESHOLD)

    while best_fitness < C_FITNESS_THRESHOLD:
        winner = pop.run(eval_genomes, 1)

        G_hall_of_fame.append(winner.fitness)
        G_ao10.append(average(G_hall_of_fame))

        graph.update(G_hall_of_fame, G_ao10, G_gen)

        best_fitness = winner.fitness

    print("Winner: ")
    print(winner)
    with open("winner-feedforward", 'wb') as f:
        pickle.dump(winner, f)
    print("Winner saved")


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
