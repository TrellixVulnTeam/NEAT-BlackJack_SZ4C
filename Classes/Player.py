class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.has_ace = False

    def hit(self, deck):
        deck.deal_to(self)

    def stay(self):
        pass

    def calc_score(self):
        score = 0
        for card in self.hand:
            score += card.value

        if score <= 11 and self.has_ace:
            score += 10

        self.score = score
        return score
