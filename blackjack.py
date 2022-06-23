import random


class Card:
    def __init__(self, suit, point_value):
        self.suit = suit
        self.point_value = point_value

    def show(self):
        print("{} of {}".format(self.point_value, self.suit))

    def __str__(self):
        return f"This card is a{self.suit} worth {self.point_value} points."

    def deal(self):
        return f"Card is a worth {self.point_value} point"
        # this is essentially the hit function"""


card = Card("Card", 6)
card.show()


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suits, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


deck = Deck()
deck.shuffle()
deck.show()
