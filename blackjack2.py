import random

CARDVALUE_PAIRS = {"Ace": [1, 11], "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
                   "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]


class Card:
    def __init__(self, suit, point_value):
        self.suit = suit
        self.point_value = point_value

    def __str__(self):
        return f"{self.point_value[0]} of {self.suit}"

    def show(self):
        print("{} of {}".format(self.point_value, self.suit))

    def determine_card_value(self, point_value):
        print(f"This card is worth {self.point_value} points ")
        for card in self.hand:
            print(f"{self.point_value}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build(SUITS, CARDVALUE_PAIRS)

    def build(self, suits, cardvalue_pairs):
        for suit in suits:
            for pair in cardvalue_pairs.items():
                card = Card(suit, pair)
                self.cards.append(card)

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_a_card(self):
        return self.cards.pop()


deck = Deck()
deck.show()
# prints the entire deck
deck.shuffle()
drawn_card = deck.draw_a_card()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def initial_deal(self, deck):
        while len(self.hand) < 2:
            self.hand.append(deck.draw_a_card())

    def hit_me(self, deck):
        self.hand.append(deck.draw_a_card())

    def showHand(self):
        print(f"{self.name}'s hand")
        for card in self.hand:
            card.show()


player1 = Player("PLAYER ONE")
dealer = Player("DEALER")

player1.initial_deal(deck)
dealer.initial_deal(deck)
player1.showHand()
dealer.showHand()
