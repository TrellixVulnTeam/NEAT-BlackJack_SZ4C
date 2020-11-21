import os
from random import random

import neat

from Classes.Deck import Deck
from Classes.Player import Player

from config import C_HANDS_PER_GENERATION
from helper import display_game_results, display_sim_results

gen = 0


def eval_genomes(genomes, config):
    global gen
    gen += 1

    players = []
    nets = []
    ge = []

    for _, g in genomes:
        g.fitness = 0

        players.append(Player())
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        ge.append(g)

    # For every hand we want to play in a simulation...
    for i in range(C_HANDS_PER_GENERATION):
        # Let's use a new deck each time
        deck = Deck()
        dealer = Player()

        # Deal two cards to each
        for player in players:
            player.hand.append(deck.top_card())

        deck.burn_top()

        for player in players:
            player.hand.append(deck.top_card())
            player.calc_score()

        deck.burn_top()

        for _ in range(2):
            deck.deal_to(dealer)

        for n, player in enumerate(players):
            d = Deck()
            d.cards = []
            for card in deck.cards:
                d.cards.append(card)

            # Activation function
            output = nets[n].activate((player.score, player.has_ace, dealer.hand[0].value))

            # While we have less than 17 points, hit, except 10% of the time stay
            while output[0] > 0.5 and player.score < 21:
                player.hit(d)
                ge[n].fitness += 0.1

        # Standard dealer rules, hit on and up to 17
        while dealer.score <= 17:
            dealer.hit(deck)

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

        best_fitness = -1000
        best_player = Player()
        for j, g in enumerate(ge):
            if g.fitness > best_fitness:
                best_fitness = g.fitness
                best_player = players[j]

        # Display the results of the final game
        if i+1 == C_HANDS_PER_GENERATION:
            display_game_results(best_player, dealer, i, msg)

        # Make sure their hands are empty
        for player in players:
            player.clear_hand()
        dealer.clear_hand()

    # Display the results of the whole simulation
    display_sim_results(best_player)


def run(path):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                path)

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    pop.add_reporter(neat.StatisticsReporter())

    winner = pop.run(eval_genomes, 200)
    print(winner)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
