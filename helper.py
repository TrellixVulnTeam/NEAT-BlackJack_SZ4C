from config import C_HANDS_PER_GENERATION


def display_game_results(player, dealer, game_number, message):
    print("Game: %s (%s)" % (game_number + 1, message))
    print("  P: %s: %s" % ([c.label for c in player.hand], player.score,))
    print("  D: %s: %s" % ([c.label for c in dealer.hand], dealer.score,))


def display_sim_results(player):
    print("Wins: %s/%s" % (player.wins, C_HANDS_PER_GENERATION))
    print("%s" % (player.wins * 100 / C_HANDS_PER_GENERATION) + "% win percentage")
    print("%s" % (player.ties * 100 / C_HANDS_PER_GENERATION) + "% tie percentage")
    print("%s" % (player.losses * 100 / C_HANDS_PER_GENERATION) + "% loss percentage")
