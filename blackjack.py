import random


class Card:
    def __init__(self, suit, point_value):
        self.suit = suit
        self.rank = point_value
        self.point_value = point_value

    def show(self):
        if self.rank == "Ace":
            self.point_value == input(
                "Should your Ace be worth 1 or 11 points?")
            print("You drew an ace")
        elif self.rank == "Jack":
            self.point_value == 10
        elif self.rank == "Queen":
            self.point_value == 10
        elif self.rank == "King":
            self.point_value == 10
        else:
            self.point_value == f"{self.point_value}"
            print("{} of {}".format(self.point_value, self.suit))


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
        #print(f"{card} is in {self.name}'s hand")

    def determine_points(self):
        for card in self.hand:
            print(card.point_value)


player1 = Player("PLAYER ONE")
dealer = Player("DEALER")

player1.initial_deal(deck)
dealer.initial_deal(deck)
player1.showHand()
dealer.showHand()
player1.determine_points()
