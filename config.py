import neat

C_HANDS_PER_GENERATION = 100
C_FITNESS_THRESHOLD = 100  # THIS HAS TO MATCH IN CONFIG-FEEDFORWARD.TXT
C_POP_PER_GEN = 200  # THIS HAS TO MATCH IN CONFIG-FEEDFORWARD.TXT
C_MIN_GRAPH_WIDTH = 10
C_NEAT_CONFIG_DEFAULTS = [neat.DefaultGenome,
                          neat.DefaultReproduction,
                          neat.DefaultSpeciesSet,
                          neat.DefaultStagnation]
