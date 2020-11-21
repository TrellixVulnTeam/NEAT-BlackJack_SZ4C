class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.has_ace = False
        self.wins = 0
        self.ties = 0
        self.losses = 0

    def hit(self, deck):
        deck.deal_to(self)

    def clear_hand(self):
        self.hand = []
        self.has_ace = False
        self.score = 0

    def calc_score(self):
        score = 0

        for card in self.hand:
            if card.value == 1:
                self.has_ace = True

        for card in self.hand:
            score += card.value

        if score <= 11 and self.has_ace:
            score += 10

        self.score = score
        return score
