from random import shuffle


class Deck(object):

    def __init__(self):

        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)] * 4
        self.shuffle()

    def deal_card(self):

        card = self.stack.pop()
        return card

    def shuffle(self):

        shuffle(self.stack)
