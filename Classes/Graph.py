from matplotlib import style
import matplotlib.pyplot as plt

from config import C_FITNESS_THRESHOLD, C_MIN_GRAPH_WIDTH
from helper import bottom_margin


class Graph:
    def __init__(self, fitness_threshold):
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.ion()

        self.fitness_threshold = fitness_threshold
        self.hall_of_fame = []
        self.threshold_line = []
        self.ao10 = []
        self.gen = 0
        self.width = 0

    def update(self, hall_of_fame, ao10, gen):
        self.hall_of_fame = hall_of_fame
        self.ao10 = ao10
        self.gen = gen

        style.use('fivethirtyeight')

        plt.title("NEAT Learning BlackJack -- Gen: %s" % self.gen)
        plt.xlabel("Generations")
        plt.ylabel("Fitness")

        self.width = C_MIN_GRAPH_WIDTH if len(hall_of_fame) - 1 < C_MIN_GRAPH_WIDTH else len(hall_of_fame) - 1
        self.threshold_line = [C_FITNESS_THRESHOLD] * (self.width + 1)

        plt.plot(self.hall_of_fame, 'g-', label="Best")
        plt.plot(self.ao10, 'b--', label="Average of 10")
        plt.plot(self.threshold_line, 'r-', label="Goal")

        plt.legend()

        plt.axis([0, self.width, bottom_margin(min(hall_of_fame)), C_FITNESS_THRESHOLD * 1.5])

        plt.draw()
        plt.pause(0.0001)

        if self.hall_of_fame[-1] > self.fitness_threshold:
            print("Press enter to exit close graph and view results")
            input()

        plt.clf()
