import random


class Card:
    def __init__(self, suit, point_value):
        self.suit = suit
        self.point_value = point_value

    def show(self):
        print("{} of {}".format(self.point_value, self.suit))
        if self.point_value == "Ace":
            self.point_value == input(
                "Should your Ace be worth 1 or 11 points? ")

    def determine_card_value(self, point_value):
        if self.cards.show() == "Ace":
            print("You drew an ace")
            self.cards.point_value == input(
                "Should your Ace be worth 1 or 11 points?")
        else:
            self.cards.point_value == self.cards.point_value
        print(f"This card is worth {self.point_value} points ")
        for card in self.hand:
            print(f"{self.point_value}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["spades", "clubs", "diamonds", "hearts"]:
            for value in range(2, 11):
                self.cards.append(Card(suits, value))
            for face_cards in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suits, face_cards))

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
# deck.show()
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
