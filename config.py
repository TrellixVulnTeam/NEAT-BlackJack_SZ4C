import neat

C_HANDS_PER_GENERATION = 100
C_GENS_PER_RUN = 200
C_FITNESS_THRESHOLD = 200
C_POP_PER_GEN = 100  # THIS HAS TO MATCH IN CONFIG-FEEDFORWARD,txt
C_MIN_GRAPH_WIDTH = 10
C_NEAT_CONFIG_DEFAULTS = [neat.DefaultGenome,
                          neat.DefaultReproduction,
                          neat.DefaultSpeciesSet,
                          neat.DefaultStagnation]
