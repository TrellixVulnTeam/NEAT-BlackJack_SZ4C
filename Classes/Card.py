class Card:
    def __init__(self, label, suit, value):
        self.label = label
        self.suit = suit
        self.value = value
        self.name = "%s of %s" % (self.label, self.suit)
